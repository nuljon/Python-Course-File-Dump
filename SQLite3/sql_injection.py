import sqlite3

# get person data from user

FirstName = raw_input("Enter your first name: ")
LastName = raw_input("Enter your last name: ")
Age = int(raw_input("Enter your age: "))

# execute insert statement  for Person table

with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	line = "INSERT INTO People VALUES('"+ FirstName +"','"+ LastName +"',"+str(Age) +")"
	c.execute(line)

# print the data from user
print(line)

	
