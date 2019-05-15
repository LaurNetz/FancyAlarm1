
#WICHTIG:
#Server bereits gestartet?
#Dieser Code ist auf dem pi

import socket
from pymongo import MongoClient
from time import strftime, gmtime, localtime, sleep
from random import randrange

while True:

    #Einstellungen
    anzeige = 2 #0 für aus, 1 für wichtiges, 2 für zusätzliches.

    #IP = "localhost" “War für Tests
    IP = "192.168.2.10"
    PORT = 50005

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, PORT))
        # send only once
        sock.send(b"Kontaktaufnahme mit Server")
        # wait for received data
        # Ab hier eigener Code
        data = ''
        data_part = ''
        while True:
            data_part = sock.recv(1024)
            if len(data_part) <= 0:
                sock.close()
                break
            data += data_part.decode("utf-8")
        print("Erhalten: "+data)
        if anzeige >= 1:
            print(type(data)) #ADG
            print(data) #ADG
    except Exception as error:
        print("Opps, something is wrong: ", error)



    with open("ProtokollDatei.txt", "r") as pfile:
        for line in file:
            line = data_json

    #Jetzt Str in JSON (=dict) umwandeln
    import json
    data_json = json.loads(data_str)
    if anzeige >= 2:
        print(data_json)
        print(type(data_json))

    #Jetzt ein bisschen schlau ausgeben.

    if anzeige >= 2:
        print("Zeit: "+data_json['time_raspi'])
        print("alarm: "+str(data_json))
        print("die datei : "+str(dateiAlsBytswenn))

    #

