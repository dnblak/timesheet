import serial
from serialchk import usePort

# Find the serial port used by RFID
serPort = usePort()

ser = serial

try:
    ser = serial.Serial(serPort, 9600, timeout=10)

    while ser.read():
        print 'serial open'

    print 'serial closed'
    ser.close()

except serial.serialutil.SerialException:
  print 'exception'