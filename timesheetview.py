import time, sys, datetime, sqlite3

sqlite_file = '/Volumes/ZAI-Enrypted/notes/timesheet/timesheet.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

for row in c.execute("SELECT * FROM timelog"):
        print row

conn.commit()
conn.close()

