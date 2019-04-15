# this UDP client runs only once
# after sending the number 42 (the byte-object of string converted integer
# it will wait till the server answers and then close the connection

import socket

mydata = str(42).encode('utf-8')

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(mydata, ("localhost", 50029))
    print("sent:", mydata)

    serverdata, serveraddr = sock.recvfrom(1024)
    print("received:", type(serverdata), serverdata, serveraddr)

    str_data = serverdata.decode()
    print("after decoding:", type(str_data), str_data)
    sock.close()
except Exception as error:
    print("Opps, something is wrong: ", error)