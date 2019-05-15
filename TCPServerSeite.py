#dieser Code läuft auf dem LapTop


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


    #Daten an MongoDB weitergeben!


from pymongo import MongoClient

# open MongoDB database and in there the collection
try:
    client = MongoClient('localhost', 27017)
    db = client['alarmanlage']
    collection = db['alarmanlagenDaten']
    print("connected to", str(db))
except:
    print("could not connect")

# generate a couple entries


emp_rec1 = {
    "Zeit":"+data_json['time_raspi']",
    "alarm":data_json,
    "die Datei":"(dateiAlsBytswenn)"
}
emp_rec2 = {
    "Zeit":"+data_json['time_raspi']",
    "alarm":data_json,
    "die Datei":"(dateiAlsBytswenn)"
}


# Insert Data
rec_id1 = collection.insert_one(emp_rec1)
rec_id2 = collection.insert_one(emp_rec2)

print("Data inserted with record ids",rec_id1," ",rec_id2)

# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)