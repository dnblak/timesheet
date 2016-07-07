import sqlite3

sqlite_file = '/Volumes/ZAI-Enrypted/notes/timesheet/timesheet.sqlite'

table_name1 = 'timelog'  # name of the table to be created

new_field = 'ID' # name of the column
field_type = 'INTEGER'  # column data type
nf01 = 'RFID'
ft01 = 'TEXT'
nf02 = 'tstamp'
ft02 = 'INTEGER'
nf03 = 'inout'
ft03 = 'INTEGER'


# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('''CREATE TABLE timelog 
	(ID INTEGER PRIMARY KEY, RFID TEXT, tstamp INTEGER, inout INTEGER)''')


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
