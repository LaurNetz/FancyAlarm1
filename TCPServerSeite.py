import socket

IP = "localhost"
PORT = 50005

try:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((IP, PORT))
    serv.listen()
    print("server started...")
    sock, addr = serv.accept()
    print("Connection from: ", addr)
    while 1:
        data = sock.recv(1024)
        if len(data) == 0:
            break     # Client closed socket
        print("received: ", data)
        data = data + " :-)fromSERVER".encode()
        sock.send(data)              # Echo received data
    sock.close()
    serv.close()
except Exception as error:
    print("Opps, something is wrong: ", error)