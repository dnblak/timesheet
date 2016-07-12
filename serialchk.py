# This file will search all the availble serial ports and look for
# specific text to identify the serial port that the RFID card
# reader is connected to. 


import serial.tools.list_ports

def usePort():
    usePort = ''
    while usePort != '':
        ports = list(serial.tools.list_ports.comports())
        portIdentifyer = "FT232R"
    
        portnames = []
        for p in ports:
            portnames.append(str(p))

            for p in portnames:
                if p.find(portIdentifyer) != -1:
                    sections = p.split(" - ")
                    usePort = sections[0]
                    return usePort