# This file will search all the availble serial ports and look for
# specific text to identify the serial port that the RFID card
# reader is connected to. 

import sys
import glob
import serial.tools.list_ports

import serial
from serial.tools import list_ports

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            print port
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def serPort2(desc):
    result = []
    for port in list(list_ports.comports()):
        try:
            s = serial.Serial(port[0])
            s.close()
            
            broken = port[1].split(" ")
            if (broken[0] == desc):
                return port[0]
        except (OSError, serial.SerialException):
            pass



def serPort(desc):
    result = []
    for port in list(list_ports.comports()):
        broken = port[1].split(" ")
        if (broken[0] == desc):
            return port[0]
        # https://forum.pjrc.com/threads/25295-Automatically-find-a-Teensy-Board-with-Python-and-PySerial

def usePort():
    ports = list(serial.tools.list_ports.comports())
    portIdentifyer = "FT232R"
    
    portnames = []
    for p in ports:
        portnames.append(str(p))

        for p in portnames:
            print p
            if p.find(portIdentifyer) != -1:
                sections = p.split(" - ")
                usePort = sections[0]

    return usePort
