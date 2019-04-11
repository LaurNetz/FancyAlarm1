import time
import grovepi

# Connect the Grove Loudness Sensor to analog port A0
# SIG,NC,VCC,GND
loudness_sensor = 0

def sound()
    while True:
        try:
            # Read the sound level
            sensor_value = grovepi.analogRead(loudness_sensor)

            print("sensor_value = %d" %sensor_value)


            # bedingung für sensor sound=True bestimmen
            if #bedingung :
                sound = True

            # bedingung für sensor sound=False bestimmen
            elif #bedingung :
                sound = False

            time.sleep(.5)
        #schreibt bei einem error einen Eintrag in die Protokolldatei inkl. Datum/Zeit
        except IOError:
            with open("ProtokollDatei.txt", "w") as pfile:
                pfile.write("Soundsensor hat einen Error" + time.strftime("%d.%m.%Y %H:%M:%S") + "\n")
            file.close
