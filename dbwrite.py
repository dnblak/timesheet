import sqlite3

sqlite_file = '/Volumes/ZAI-Enrypted/notes/timesheet/timesheet.sqlite'

table_name1 = 'timelog'  # name of the table to be created

RFID = raw_input('Enter your RFID: ')
tstamp = raw_input('Enter your timestamp: ')


# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


c.execute("INSERT INTO timelog (RFID, tstamp, inout) VALUES ('"+RFID+"', '"+tstamp+"', '1')")



# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
