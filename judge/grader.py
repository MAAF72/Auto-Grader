"""
Script for auto grading submission
"""
from time import time, sleep
from os import remove, path, getcwd
from subprocess import TimeoutExpired, CalledProcessError, run, PIPE
import sqlite3

def delete_file(file):
    """
    Delete the file if exist
    """
    if path.isfile(file):
        remove(file)

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
    if language == 'Golang':
        command = 'go build -o Temp-Program/{0}.exe Submission/{0}.go'.format(file_name)
    elif language == 'C++':
        command = 'g++ -std=gnu++11 -O2 -g -lm "Submission/{0}.cpp" -o Temp-Program/{0}'.format(file_name)
    elif language == 'C':
        command = 'gcc -std=gnu99 -O2 -g -lm "Submission/{0}.cpp" -o Temp-Program/{0}'.format(file_name)

    if command:
        try:
            process = run(command, stdin=None, stdout=None, stderr=PIPE, check=True)

            if process.returncode == 0:
                return 'Success', None

            return 'CTE', process.stderr

        except CalledProcessError as error:
            return 'UNE', error.output()

    return 'CTE', 'The language is not allowed'

def run_test_case(args):
    """
    Run the program with test case
    """
    try:
        with open(args['INPUT_FILE'], 'r') as input_string, open(args['OUTPUT_FILE'], 'w') as output_string:
            command = r'{}\{}'.format(r'{}\Temp-Program'.format(getcwd()), args['FILE_NAME'])
            start_time = time()
            process = run(
                command,
                stdin=input_string,
                stdout=output_string,
                stderr=PIPE,
                timeout=args['TIMEOUT'],
                check=True
            )
            run_time = round((time() - start_time), 2)

            if process.returncode == 0:
                return 'Success', None, run_time

            return 'RTE', process.stderr, run_time

    except TimeoutExpired as tle:
        return 'TLE', tle, 2
    except CalledProcessError as cpe:
        return 'UNE', cpe.output(), run_time

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
                'INPUT_FILE' : 'TC-In/{}.txt'.format(args['TEST_CASE'][0][0]),
                'OUTPUT_FILE' : '{}_DummyRun.txt'.format(args['FILE_NAME']),
                'TIMEOUT' : args['TIMEOUT']
            }
        )
        delete_file('{}_DummyRun.txt'.format(args['FILE_NAME']))

        for i in args['TEST_CASE']:
            input_file = 'TC-In/{}.txt'.format(i[0])
            key = 'TC-Out/{}.txt'.format(i[0])
            output_file = 'Temp-Out/{}_{}.txt'.format(args['FILE_NAME'], i[0])

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
    delete_file(r'{}\Temp-Program\\{}.exe'.format(getcwd(), args['FILE_NAME']))
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
                        'TIMEOUT' : i[4],
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
    DB_FILE = '../website/db.sqlite3'
    DB_CON = sqlite3.connect(DB_FILE, isolation_level=None)
    grade(DB_CON.cursor(), 0)

except sqlite3.Error as error:
    print('Error while connecting to database', error)
except KeyboardInterrupt:
    pass
else:
    if DB_CON.is_connected():
        DB_CON.cursor().close()
        DB_CON.close()
        print('Database connection is closed.')
finally:
    print('Finish grading: {}s'.format(round(time() - START, 2)))
