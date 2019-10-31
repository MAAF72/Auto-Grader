"""
Script for auto grading submission
"""
from time import time, sleep
from os import remove, path, name as os_name
from subprocess import TimeoutExpired, CalledProcessError, SubprocessError, run, PIPE
import sqlite3
import re

if os_name != 'nt':
    import limit

def cmdline_split(s, platform='this'):
    """Multi-platform variant of shlex.split() for command-line splitting.
    For use with subprocess, for argv injection etc. Using fast REGEX.

    platform: 'this' = auto from current platform;
              1 = POSIX; 
              0 = Windows/CMD
              (other values reserved)
    """
    if platform == 'this':
        platform = (os_name != 'nt')
    if platform == 1:
        RE_CMD_LEX = r'''"((?:\\["\\]|[^"])*)"|'([^']*)'|(\\.)|(&&?|\|\|?|\d?\>|[<])|([^\s'"\\&|<>]+)|(\s+)|(.)'''
    elif platform == 0:
        RE_CMD_LEX = r'''"((?:""|\\["\\]|[^"])*)"?()|(\\\\(?=\\*")|\\")|(&&?|\|\|?|\d?>|[<])|([^\s"&|<>]+)|(\s+)|(.)'''
    else:
        raise AssertionError('unkown platform %r' % platform)

    args = []
    accu = None   # collects pieces of one arg
    for qs, qss, esc, pipe, word, white, fail in re.findall(RE_CMD_LEX, s):
        if word:
            pass   # most frequent
        elif esc:
            word = esc[1]
        elif white or pipe:
            if accu is not None:
                args.append(accu)
            if pipe:
                args.append(pipe)
            accu = None
            continue
        elif fail:
            raise ValueError("invalid or incomplete shell string")
        elif qs:
            word = qs.replace('\\"', '"').replace('\\\\', '\\')
            if platform == 0:
                word = word.replace('""', '"')
        else:
            word = qss   # may be even empty; must be last

        accu = (accu or '') + word

    if accu is not None:
        args.append(accu)

    return args

def delete_file(file):
    """
    Delete the file if exist
    """
    for _ in range(10):
        try:
            if path.isfile(file):
                remove(file)
        except Exception as error:
            sleep(5)
            print("Delete failed, retrying...", error)
        else:
            break

def compare_file(file1, file2):
    """
    Compare two file, line by line
    """
    line1 = True
    line2 = True
    with open(file1, 'r') as f_1, open(file2, 'r') as f_2:
        while line1 and line2:
            line1 = f_1.readline()
            line2 = f_2.readline()
            if line1 != line2:
                return False
    return True

def compile_file(file_name, language):
    """
    Compile the file source
    """
    command = None
    temp_dir = path.join('Temp-Program', '{}.judge'.format(file_name))
    if language == 'Golang':
        command = 'go build -o {} {}'.format(
            temp_dir,
            path.join('Submission', '{}.go'.format(file_name))
        )
    elif language == 'C++':
        command = 'g++ -std=gnu++11 -O2 -g -lm "{}" -o {}'.format(
            path.join('Submission', '{}.cpp'.format(file_name)),
            temp_dir
        )
    elif language == 'C':
        command = 'gcc -std=gnu99 -O2 -g -lm "{}" -o {}'.format(
            path.join('Submission', '{}.c'.format(file_name)),
            temp_dir
        )

    if command:
        try:
            process = run(
                cmdline_split(command),
                stdin=None,
                stdout=None,
                stderr=PIPE,
                shell=False
            )

            if process.returncode == 0:
                return 'Success', None

            return 'CTE', process.stderr

        except CalledProcessError as cpe:
            if cpe.returncode == 3:
                return 'ACE', cpe
            return 'UNE', cpe
        except SubprocessError as spe:
            return 'UNE', spe

        except Exception as error:
            print(error)

    return 'CTE', 'The language is not allowed'

def run_test_case(args):
    """
    Run the program with test case
    """
    try:
        with open(args['INPUT_FILE'], 'r') as fin, open(args['OUTPUT_FILE'], 'w') as fout:
            command = path.join('Temp-Program', '{}.judge'.format(args['FILE_NAME']))
            start_time = time()
            process = None
            if os_name != 'nt':
                limit.change_max_virtual_memory(256 * 1024 * 1024)
                process = run(
                    cmdline_split(command),
                    stdin=fin,
                    stdout=fout,
                    stderr=PIPE,
                    timeout=args['TIMEOUT'],
                    preexec_fn=limit.limit_virtual_memory
                )
            else:
                process = run(
                    cmdline_split(command),
                    stdin=fin,
                    stdout=fout,
                    stderr=PIPE,
                    timeout=args['TIMEOUT']
                )

            run_time = round((time() - start_time), 2)

            if process.returncode == 0:
                return 'Success', None, run_time
            #2 = Pola Aneh make 100000000 array in golang Linux
            #-6 = Kodingan Restaurant.cpp dimasukin ke Pola Aneh Linux
            #3 = Kodingan Restaurant.cpp dimasukin ke Pola Aneh Windows || std::bad_array_new_length
            #print("process", process)
            #print("process args", process.args)
            #print("process returncode", process.returncode)
            #print("process stderr", process.stderr)
            return 'RTE', process.returncode, run_time

    except TimeoutExpired as tle:
        return 'TLE', tle, 2.00
    except CalledProcessError as cpe:
        print("CPE, returncode:", cpe.returncode)
        if cpe.returncode == 3:
            return 'ACE', cpe, 0.00
        elif cpe.returncode == -11:
            return 'MLE', cpe, 0.00
        return 'UNE', cpe, 0.00
    except SubprocessError as spe:
        print("SPE, returncode:", spe.returncode)
        return 'UNE', spe, 0.00

    except Exception as error:
        print(error)

def judge(args):
    """
    Test the submission with test cases
    """
    score = 0
    status = None

    #Compile
    compile_result, compile_error = compile_file(args['FILE_NAME'], args['LANGUAGE'])
    if compile_result == 'Success':
        #Test with all TC

        if args['LANGUAGE'] == 'Golang':
            args['TIMEOUT'] *= 2

        #Dummy run
        _, _, _ = run_test_case(
            {
                'FILE_NAME' : args['FILE_NAME'],
                'INPUT_FILE' : path.join('TC-In', '{}.txt'.format(args['TEST_CASE'][0][0])),
                'OUTPUT_FILE' : '{}_DummyRun.txt'.format(args['FILE_NAME']),
                'TIMEOUT' : args['TIMEOUT']
            }
        )
        delete_file('{}_DummyRun.txt'.format(args['FILE_NAME']))

        for i in args['TEST_CASE']:
            input_file = path.join('TC-In', '{}.txt'.format(i[0]))
            key = path.join('TC-Out', '{}.txt'.format(i[0]))
            output_file = path.join('Temp-Out', '{}_{}.txt'.format(args['FILE_NAME'], i[0]))

            #Run with TC
            run_result, run_error, run_time = run_test_case(
                {
                    'FILE_NAME' : args['FILE_NAME'],
                    'INPUT_FILE' : input_file,
                    'OUTPUT_FILE' : output_file,
                    'TIMEOUT' : args['TIMEOUT']
                }
            )
            if run_result == 'Success':
                if compare_file(key, output_file):
                    score += 1
                    print('TC {} passed in {}s'.format(i[0], run_time))
                else:
                    print('TC {} not passed in {}s'.format(i[0], run_time))
            else:
                print('TC {} {} {}'.format(i[0], run_result, run_error))
                status = run_result

            #Delete output_file
            delete_file(output_file)

        if score == len(args['TEST_CASE']):
            status = 'AC'
        elif status is None:
            status = 'WA'

    else:
        print('Compile Failed:', compile_result)
        print(compile_error)
        status = compile_result

    #Delete program
    delete_file(path.join('Temp-Program', '{}.judge'.format(args['FILE_NAME'])))
    return round((score / len(args['TEST_CASE']) * 100), 2), status

def get_test_case(cursor, problem_id):
    """
    Get the test case from database
    """
    cursor.execute(
        '''
        SELECT
            name
        FROM
            apps_testcase
        WHERE
            problem_id = ?
        ''',
        (problem_id,)
    )

    return cursor.fetchall()

def grade(cursor, host):
    """
    Grade the program
    """
    while True:
        print('Grading...')
        cursor.execute(
            '''
            SELECT
                apps_submission.id,
                apps_submission.problem_id,
                apps_submission.name,
                apps_submission.language,
                apps_problem.time,
                apps_problem.memory
            FROM
                apps_submission,
                apps_problem
            WHERE
                apps_submission.host = ?
                AND apps_submission.status = ?
                AND apps_submission.problem_id = apps_problem.id
            ''',
            (host, 'PEN')
        )
        query_result = cursor.fetchall()
        if len(query_result) == 0:
            print('Queue submission is empty, sleep for 10 seconds')
            sleep(10) #Sleep for 10 seconds if the queue is empty
            print('Getting queue submission...')
        else:
            for i in query_result:

                #Make sure program file, input_file, and key are present
                test_case = get_test_case(cursor, i[1])
                print('Judging SubmissionID: {}'.format(i[0]))
                score, status = judge(
                    {
                        'TEST_CASE' : test_case,
                        'FILE_NAME' : i[2],
                        'LANGUAGE' : i[3],
                        'TIMEOUT' : i[4]
                    }
                )
                if status:
                    print('Update SubmissionID:', i[0])
                    cursor.execute(
                        '''
                        UPDATE
                            apps_submission
                        SET
                            score = ?,
                            status = ?
                        WHERE
                            id = ?
                        ''',
                        (score, status, i[0])
                    )
try:
    START = time()
    DB_FILE = path.join('..', 'website', 'db.sqlite3')
    DB_CON = sqlite3.connect(DB_FILE, isolation_level=None)
    grade(DB_CON.cursor(), 0)

except sqlite3.Error as error:
    print('Error while connecting to database', error)
except KeyboardInterrupt:
    pass
except Exception as error:
    print(error)
else:
    if DB_CON.is_connected():
        DB_CON.cursor().close()
        DB_CON.close()
        print('Database connection is closed.')
finally:
    print('Finish grading: {}s'.format(round(time() - START, 2)))
