import sqlite3

sqlite_file = '/Volumes/ZAI-Enrypted/notes/timesheet/timesheet.sqlite'

tblname = 'timelogA'  # name of the table to be created

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute("CREATE TABLE '"+tblname+"' (ID INTEGER PRIMARY KEY AUTOINCREMENT, RFID TEXT, tstamp INTEGER, inout INTEGER)")
c.execute("INSERT INTO `main`.`"+tblname+"` (`RFID`, `tstamp`, `inout`) VALUES ('0',0,0)")

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
