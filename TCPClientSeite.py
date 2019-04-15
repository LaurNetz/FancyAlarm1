import socket
import time

IP = "localhost"
PORT = 50005

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    # send only once
    sock.send(b"I wait for an echo")
    # wait for received data
    data = sock.recv(1024)
    print("received: ", data)
    # send second string as byte
    sock.send(b"thank you - I got the message...")
    data = sock.recv(1024)
    print("received: {0}".format(data))
    sock.close()
except Exception as error:
    print("Opps, something is wrong: ", error)
