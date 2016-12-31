import sqlite3

rosterValues = (
    ("Jean-Baptiste Zorg","Human",122),
    ("Korban Dallas","Meat Popsicle",100),
    ("Ak'not","Mangalore",-5))

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?,?,?)",rosterValues)
    # commit change and check that we have what we expect here so far
   # connection.commit() wasn't necessary
    c.execute("SELECT * FROM Roster")
    for row in c.fetchall():
        print row
    # update korban to human
    c.execute("UPDATE Roster SET Species = ? WHERE Name =?", ('Human','Korban Dallas'))
    # commit change and display humans
   # connection.commit() - wasn't necessary
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in c.fetchall():
        print row
        
    
    
    
    

              



	
