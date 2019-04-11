import time

with open("ProtokollDatei.txt", "w") as pfile:
    pfile.write("peace" + time.strftime("%d.%m.%Y %H:%M:%S") + "\n")
