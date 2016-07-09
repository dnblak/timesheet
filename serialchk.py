import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())

portnames = []
for p in ports:
    portnames.append(str(p))

for p in portnames:
    if p.find("FT232R") != -1:
        sections = p.split(" - ")
        usePort = sections[0]

print usePort