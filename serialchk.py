# This file will search all the availble serial ports and look for
# specific text to identify the serial port that the RFID card
# reader is connected to. 

import sys
import glob
import serial


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
            
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def usePort():
    usePort = ''
    while usePort == '':
        ports = list(serial.tools.list_ports.comports())
        portIdentifyer = "FT232R"
        comMethod = "tty"
    
        portnames = []
        for p in ports:
            portnames.append(str(p))

            for p in portnames:
                print p
                if p.find(portIdentifyer) != -1:
                    sections = p.split(" - ")
                    print sections
                    usePort = sections[0]
                    print usePort
                    subSec = usePort[0].split(".")
                    if subSec[0] == "tty":
                        return usePort