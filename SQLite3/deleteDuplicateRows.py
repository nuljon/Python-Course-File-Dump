import sqlite3

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
# lets clean out the duplicate rows, preserving the row with the lowest rowid
    c.execute("DELETE FROM People WHERE rowid NOT IN (SELECT min(rowid) FROM People GROUP BY FirstName, LastName, Age)")
# prove no dups visually
    c.execute("SELECT * FROM People")
#    for row in c.fetchall():
        #print these
#       print row
    while True:
        row = c.fetchone()
        if row is None:
            break
        print row
              



	
