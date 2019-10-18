TaskID = 3

for i in range(10) :
	Query = "INSERT INTO test_case (TaskID, Input, Output) VALUES({}, '{}', '{}');".format(TaskID, "Pizza" + str(i), "Pizza" + str(i))
	print(Query)
	