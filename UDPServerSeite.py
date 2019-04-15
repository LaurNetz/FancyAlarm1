import socket
import time

UDPIP = "localhost"
UDPPORT = 50029

try:
    serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv.bind((UDPIP, UDPPORT))
    print("server waiting...")

    data, addr = serv.recvfrom(1024)
    ddata = data.decode('utf-8')
    print("received: ", type(ddata), ddata, addr)
    serv.sendto(b'Hallo, hier spricht der fudi SERVER', addr)
    print("sent Hallo")
    serv.close()
except Exception as error:
    print("Opps, something is wrong: ", error)