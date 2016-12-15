from __future__ import unicode_literals
import sqlite3

# queue some people tuples 

peopleValues = (
    ('Frank','LLoyd-Wright',125),
    ('George','Burns',105),
    ('John','Pantera',52))

# insert the tuples in db

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executemany("INSERT INTO People VALUES(?,?,?)",peopleValues)
# first select all the people we have accumulated
    c.execute("SELECT * FROM People")
    for row in c.fetchall():
        # print the data selected
        print row
# second just select people names who are over 50
    c.execute("SELECT FirstName, LastName FROM People WHERE Age >50")
    for row in c.fetchall():
        #print these
        print row
        
              



	
