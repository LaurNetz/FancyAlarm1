import time
import grovepi

# Connect the Grove PIR Motion Sensor to digital port D8
# SIG,NC,VCC,GND
pir_sensor = 8

#Diese Variable nutzen wir in MainCode um alarm auszuläsen
motion = True

grovepi.pinMode(pir_sensor,"INPUT")
def MotionFunk():
    while True:
        try:
            # Sense motion, usually human, within the target range
            if grovepi.digitalRead(pir_sensor):
                print 'Motion Detected'
            else:
                print '-'

            # bedingung für sensor motion=True bestimmen
            if  # bedingung :
                motion = True

            # bedingung für sensor sound=False bestimmen
            elif  # bedingung :
                motion = False


            # if your hold time is less than this, you might not see as many detections
            time.sleep(.2)
         #schreibt bei einem error einen Eintrag in die Protokolldatei inkl. Datum/Zeit
        except IOError:
            with open("ProtokollDatei.txt", "w") as pfile:
                pfile.write("Motion Sensor hat einen Error" + time.strftime("%d.%m.%Y %H:%M:%S") + "\n")

