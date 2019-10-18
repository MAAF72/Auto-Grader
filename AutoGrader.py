from time import time
from os import remove, path
from mysql import connector
from subprocess import TimeoutExpired, CalledProcessError, run, PIPE

TempProgram = "D:\Auto Grader\Temp-Program"

GetTime = lambda : time()

def DeleteFile(File) :
	if path.isfile(File) :
		remove(File)
		
#Error kalau ada baris baru dibandingkan dengan tidak ada baris baru
def Compare(File1, File2) :
	Line1 = True
	Line2 = True
	with open(File1, 'r') as F1, open(File2, 'r') as F2 :
		while Line1 and Line2 :
			Line1 = F1.readline()
			Line2 = F2.readline()
			if Line1 != Line2 :
				return False
	return True

def Compile(FileName) :
	try :
		Command = "go build -o Temp-Program/{} Submission/{}.go".format(FileName, FileName)
		Process = run(Command, stdin = None, stdout = None, stderr = PIPE)
		
		if Process.returncode == 0 :
			return "Success", None
		else :
			return "Compile Error : {}".format(Process.returncode), Process.stderr
	except CalledProcessError as Error:
		return "Error Unknown", Error.output()
	
	#return "???", "INI NGAPA ANJENG KOK BISA BYPASS KESINI"
	
def RunTC(FileName, Input, Output) :
	# bufsize = 65536
	try :
		with open(Input, 'r') as FileInput, open(Output, 'w') as FileOutput :
			Command = "{}\{}".format(TempProgram, FileName)
			StartTime = GetTime()
			Process = run(Command, stdin = FileInput, stdout = FileOutput, stderr = PIPE, timeout = 10)
			RunTime = round((GetTime() - StartTime), 2)
		if Process.returncode == 0 :
			return "Success", None, RunTime
		else :
			return "Run Time Error : {}".format(Process.returncode), Process.stderr, RunTime
	except TimeoutExpired as TLE :
		return "Time Limit Exceeded", TLE, 2
	except CalledProcessError as CPE :
		return "Called Process Error", CPE.output(), RunTime
	
	#return "???", "INI NGAPA ANJENG KOK BISA BYPASS KESINI"		

def Judge(TC, FileName) :
	Score = 0
	Status = None
	
	#Compile
	CompileResult, CompileError = Compile(FileName)
	if CompileResult == "Success" :
		#Test with all TC
		
		#Dummy run
		_, _, _ = RunTC(FileName, "TC-In/{}.txt".format(TC[0][0]), "{}_DummyRun.txt".format(FileName))
		DeleteFile("{}_DummyRun.txt".format(FileName))
		
		for i in TC :
			Input = "TC-In/{}.txt".format(i[0])
			Key = "TC-Out/{}.txt".format(i[1])
			Output = "Temp-Out/{}_{}.txt".format(FileName, i[0])
		
			#Run with TC
			RunResult, RunError, RunTime = RunTC(FileName, Input, Output)
			
			if RunResult == "Success" :
				if Compare(Key, Output) :
					Score += 1
					print("TC {} passed in {}s".format(i[0], RunTime))
				else :
					print("TC {} not passed in {}s".format(i[0], RunTime))
			else :
				print("TC {} {} {}".format(i[0], RunResult, RunError))
				Status = RunResult
				
			#Delete output
			DeleteFile(Output)
		
		if Score == len(TC) :
			Status = "Accepted"
		elif Status is None :
			Status = "Wrong Answer"
	
	else :
		print("Compile Failed : ", CompileResult)
		print(CompileError)
		Status = CompileResult
		
	#Delete program
	DeleteFile(TempProgram + '\\' + FileName)
	return round(((Score / len(TC)) * 100), 2), Status
	
def GetTestCase(Cursor, TaskID) :
	#Another version, get TC from file, a txt file with Input links and Output links
	Query = "SELECT Input, Output FROM test_case WHERE TaskID = {}".format(TaskID)
	Cursor.execute(Query)
	QueryResult = Cursor.fetchall()
	
	return QueryResult
	
def Grade(Cursor, TaskID, FileName, Language) :
	Query = "INSERT INTO submission (TaskID, FileName, Language) VALUES ({}, '{}', '{}')".format(TaskID, FileName, Language)
	Cursor.execute(Query)
	
	SubmissionID = Cursor.lastrowid
	
	print("SubmissionID : ", SubmissionID)
	
	TC = GetTestCase(Cursor, TaskID)
	
	Score, Status = Judge(TC, FileName)
	
	Query = "UPDATE submission SET Score = {}, Status = '{}' WHERE ID = {}".format(Score, Status, SubmissionID)
	Cursor.execute(Query)
	
	print("Score : ", Score)
	
DBConfig = {
	"user": "root",
	"password": "",
	"host": "localhost",
	"database": "AutoGrader"
}

try :

	DBCon = connector.connect(**DBConfig)
	
	Cursor = DBCon.cursor()
	
	Grade(Cursor, 3, "PizzaHutDelivery_1301180154", "Go")
	
	DBCon.commit()
	
except connector.Error as Error :
	#DBCon.rollback()
	print("Error while connecting to MySQL", Error)
finally :
	if DBCon.is_connected() :
		Cursor.close()
		DBCon.close()
		print("MySQl connection is closed.")