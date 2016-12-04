import time, sys, datetime, sqlite3

def secTOhms(elapse):
    if (elapse < 0):
        posneg = "-"
        elapse = elapse*(-1)
    else:
        posneg = "+"
    h=m=s=0
    m, s = divmod(elapse, 60)
    h, m = divmod(m, 60)
    return h, m, s, posneg

def dayTime(elapseTime):
    eightHours = 8*60*60
    timeLeft   = eightHours - elapseTime
    h, m, s, pn = secTOhms(elapseTime)
    hL, mL, sL, pn = secTOhms(timeLeft)
    print "Total time for the Day: %d:%02d:%02d" % (h, m, s); 
    print "Time Left for the Day:"+ pn +"%d:%02d:%02d" % (hL, mL, sL); 
    print '----------'

sqlite_file = '/Volumes/ZAI-Encrypted/notes/timesheet/timesheet.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

start = 0
elapsed = 0
elapsedDay = 0
datestamp = ''
day = ''
lastday = ''
io = ''


for row in c.execute("SELECT ID, RFID, tstamp, inout FROM timelog"):
    h=m=s=0
    ID      = row[0]
    RFID    = row[1]
    tstamp  = row[2]
    inout   = row[3]
    datestamp = datetime.datetime.fromtimestamp(int(row[2])).strftime('%Y-%m-%d %H:%M:%S')
    day = datetime.datetime.fromtimestamp(int(row[2])).strftime('%d')
    
    if (inout == 1):
        start = tstamp
        io = "In"
    else:
        io = "Out"
        elapsed = tstamp - start

    h, m, s, pn = secTOhms(elapsed)
   

    if (day != lastday):
        dayTime(elapsedDay)
        elapsedDay = 0
        
    
    print row[0], ": ", datestamp, " : ", io, row[3]
    if (inout == 0):
        print "Time Logged: %d:%02d:%02d" % (h, m, s)
        elapsedDay += elapsed
    
    lastday = day

if (inout == 1):
    unxtme = time.time()
    elapsed = unxtme - start
    h, m, s, pn = secTOhms(elapsed)
    print "Current working time: %d:%02d:%02d" % (h, m, s)
    elapsedDay += elapsed
    dayTime(elapsedDay)

if (day == lastday and inout == 0):
    dayTime(elapsedDay)

conn.commit()
conn.close()

