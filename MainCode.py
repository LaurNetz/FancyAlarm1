import loudnesssensor
import motionsensor
import cameraaktor

# Die zwei Variablen Sound und Motion Zustandsfefinition. IN den Codes der Sensoren muss also die jeweilige Zustände gesetzt werden

def sensor:
    if (Sound = False) + (Motion = False):
    sensor = False
    if (Sound = True) + (Motion = True):
    sensor = True
    if (Sound = False) + (Motion = False):
    sensor = False
    if (Sound = False) + (Motion = True):
    sensor = False

while sensor = FALSE:
    with open("ProtokollDatei.txt", "w") as pfile:
    pfile.write("peace" + date + time + "\n")
    file.close

    if sensor = TRUE:
        cam()
        stream()
        with open("ProtokollDatei.txt", "r") as pfile:
        pfile.write("peace" + date + time + "\n")
        file.close

