import loudnesssensor
import motionsensor
import cameraaktor
# Time Modul importieren (für die Protokoll Datei)
import time

# Die zwei Variablen Sound und Motion Zustandsfefinition. IN den Codes der Sensoren muss also die jeweilige Zustände gesetzt werden

def sensor:
    if (sound = False) + (motion = False):
    sensor = False
    if (sound = True) + (motion = True):
    sensor = True
    if (sound = False) + (motion = False):
    sensor = False
    if (sound = False) + (motion = True):
    sensor = False

while sensor = FALSE:
    with open("ProtokollDatei.txt", "w") as pfile:
    pfile.write("peace" + time.strftime("%d.%m.%Y %H:%M:%S") + "\n")
    file.close

# print(time.strftime("%d.%m.%Y %H:%M:%S"))


    if sensor = TRUE:
        cam()
        stream()
        with open("ProtokollDatei.txt", "r") as pfile:
        pfile.write("peace" + time.strftime("%d.%m.%Y %H:%M:%S") + "\n")
        file.close

