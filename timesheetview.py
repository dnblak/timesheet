import time, sys, datetime, sqlite3

sqlite_file = '/Volumes/ZAI-Enrypted/notes/timesheet/timesheet.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

start = 0
elapsed = 0

for row in c.execute("SELECT ID, RFID, tstamp, inout FROM timelog"):
        print row[0], ": ", row[1], row[2], row[3]
        ID      = row[0]
        RFID    = row[1]
        tstamp  = row[2]
        inout   = row[3]
        datestamp = datetime.datetime.fromtimestamp(int(row[2])).strftime('%Y-%m-%d %H:%M:%S')
        if (inout == 0):
            io = "Out"
        else:
            io = "In"
        if (inout == 1):
            start = tstamp
        else:
            elapsed = tstamp - start
            print elapsed
            m, s = divmod(elapsed, 60)
            h, m = divmod(m, 60)
            print "%d:%02d:%02d" % (h, m, s)

conn.commit()
conn.close()

