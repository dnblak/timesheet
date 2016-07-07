import time, sys, serial, datetime, sqlite3

serial = serial.Serial("/dev/tty.usbserial-A105BMXG", baudrate=9600)

sqlite_file = '/Volumes/ZAI-Enrypted/notes/timesheet/timesheet.sqlite'
code = ''

while True:
        data = serial.read()
        if data == '\r':
		unxtme = str(time.time())
		timestmp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
		print(code)
		print(timestmp)
		
		conn = sqlite3.connect(sqlite_file)
		c = conn.cursor()
		c.execute("INSERT INTO `main`.`timelog` (`RFID`, `tstamp`, `inout`) VALUES (code,timestmp,1)")
		conn.commit()
		conn.close()

        else:
                code = code + data
