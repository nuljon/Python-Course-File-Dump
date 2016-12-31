import sqlite3

# get person data from user and insert into A TUPLE

firstName = raw_input("Enter your first name: ")
lastName = raw_input("Enter your last name: ")
age = int(raw_input("Enter your age: "))
personData = (firstName, lastName, age)
# execute insert statement of user input into People table

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?,?,?)",personData)
# with sqlite3.connect('test_database.db') as connection:
    c.execute("UPDATE People SET Age = ? WHERE FirstName=? AND LastName=?",(25,'Luigi','Vercotti'))
# print the data from user
print(personData)



	
