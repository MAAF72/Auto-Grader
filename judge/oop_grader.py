from time import time, sleep
from os import remove, path
from subprocess import TimeoutExpired, CalledProcessError, SubprocessError, run, PIPE
import limit
import shlex

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
            print('Delete failed, retrying...', error)
        else:
            break

class Submission:
    def __init__(self, args):
        self.id = args[0]
        self.problem = args[1]
        self.file = args[2]
        self.language = args[3]
        self.time_limit = args[4]
        self.memory_limit = args[5]
        self.test_cases = args[6]

    def compile(self):
        """
        Compile the file source
        """
        command = None
        temp_dir = path.join('TempProgram', '{}.judge'.format(self.file))
        if self.language == 'GO':
            command = 'go build -o {} {}'.format(
                temp_dir,
                path.join('Submission', '{}.go'.format(self.file))
            )
        elif self.language == 'C++':
            command = 'g++ -std=gnu++11 -O2 -g -lm "{}" -o {}'.format(
                path.join('Submission', '{}.cpp'.format(self.file)),
                temp_dir
            )
        elif self.language == 'C':
            command = 'gcc -std=gnu99 -O2 -g -lm "{}" -o {}'.format(
                path.join('Submission', '{}.c'.format(self.file)),
                temp_dir
            )
        else:
            return 'CTE', 'The language is not allowed'

        try:
            process = run(
                shlex.split(command),
                stdin=None,
                stdout=None,
                stderr=PIPE,
                shell=False
            )

            if process.returncode == 0:
                return 'SUCCESS', None

            return 'CTE', process.stderr

        except CalledProcessError as cpe:
            if cpe.returncode == 3:
                return 'ACE', cpe
            return 'UNE', cpe
        except SubprocessError as spe:
            return 'UNE', spe

        except Exception as error:
            pass
            #print(error)

    def test(self, input_file, output_file):
        """
        Run the program with test case
        """
        try:
            with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
                command = path.join('TempProgram', '{}.judge'.format(self.file))
                start_time = time()
                process = None
                limit.change_max_virtual_memory(self.memory_limit * 1024 * 1024)
                process = run(
                    shlex.split(command),
                    stdin=fin,
                    stdout=fout,
                    stderr=PIPE,
                    timeout=self.time_limit,
                    preexec_fn=limit.limit_virtual_memory
                )

                run_time = round((time() - start_time), 2)
                
                if process.returncode == 0:
                    return 'SUCCESS', None, run_time

                return 'RTE', process.returncode, run_time
        except TimeoutExpired as tle:
            return 'TLE', tle, 2.00
        except CalledProcessError as cpe:
            #print('CPE, returncode:', cpe.returncode)
            if cpe.returncode == 3:
                return 'ACE', cpe, 0.00
            elif cpe.returncode == -11:
                return 'MLE', cpe, 0.00
            return 'UNE', cpe, 0.00
        except SubprocessError as spe:
            #print('SPE, returncode:', spe.returncode)
            return 'UNE', spe, 0.00
        except Exception as error:
            pass
            #print(error)

    def judge(self):
        """
        Test the submission with test cases
        """
        score = 0
        status = None
        
        compile_result, compile_error = self.compile()         
        
        if compile_result == 'SUCCESS':
            #Test with all TC

            #Dummy run
            self.test(path.join('TCIn', '{}.txt'.format(self.test_cases[0][0])), '{}_DummyRun.txt'.format(self.file))
            delete_file('{}_DummyRun.txt'.format(self.file))

            for tc in self.test_cases:
                input_file = path.join('TCIn', '{}.txt'.format(tc[0]))
                key = path.join('TCOut', '{}.txt'.format(tc[1]))
                output_file = path.join('TempOut', '{}_{}.txt'.format(self.file, tc[0]))

                #Run with TC
                run_result, run_error, run_time = self.test(input_file, output_file)
                if run_result == 'SUCCESS':
                    if compare_file(key, output_file):
                        score += 1
                        #print('TC {} passed in {}s'.format(tc[0], run_time))
                    #else:
                        #print('TC {} not passed in {}s'.format(tc[0], run_time))
                else:
                    print('TC {} {} {}'.format(tc, run_result, run_error))
                    status = run_result

                #Delete output_file
                delete_file(output_file)

            if score == len(self.test_cases):
                status = 'AC'
            elif status is None:
                status = 'WA'

        else:
            print('Compile Failed:', compile_result)
            print(compile_error)
            status = compile_result

        #Delete program
        delete_file(path.join('TempProgram', '{}.judge'.format(self.file)))

        return self.id, round((score / len(self.test_cases) * 100), 2), status

#subs = Submission([1, 1, '6a6d5544-f2e8-455d-9691-789cdb25bb2f', 'C++', 1, 256, ['RestaurantNekoya (1)', 'RestaurantNekoya (2)', 'RestaurantNekoya (3)', 'RestaurantNekoya (4)', 'RestaurantNekoya (5)', 'RestaurantNekoya (6)', 'RestaurantNekoya (7)', 'RestaurantNekoya (8)', 'RestaurantNekoya (9)', 'RestaurantNekoya (10)']])
#print(subs.judge())
   