import time
import grovepi
from picamera import PiCamera

def start():
    # Connect the Grove PIR Motion Sensor to digital port D8
    # SIG,NC,VCC,GND
    pir_sensor = 8
    loudness_sensor = 0
    led = 3
    camera = PiCamera()
    camera.resolution = (1024, 768)

    grovepi.pinMode(pir_sensor,"INPUT")

    while True:
        try:
            # Sense motion, usually human, within the target range
            if grovepi.digitalRead(pir_sensor) and grovepi.analogRead(loudness_sensor) > 30:
                grovepi.digitalWrite(led, 1)  # Send HIGH to switch on LED
                print ("LED ON!")
                camera.capture('/home/pi/Desktop/live2.jpg')
                print("Image Shot")
                with open("ProtokollDatei.txt", "w") as pfile:
                    pfile.write("Alarm ein Bild wurde aufgenommen" + time.strftime("%d.%m.%Y %H:%M:%S") + "\n")
                time.sleep(0.5)
                grovepi.digitalWrite(led, 0)  # Send LOW to switch off LED

            else:
                print '-'

            # if your hold time is less than this, you might not see as many detections
            time.sleep(0.5)

        except IOError as error:
print("Error in Surveillance " + error)















#altes
    while True:
        try:
            # Sense motion, usually human, within the target range
            if grovepi.digitalRead(pir_sensor) and grovepi.analogRead(loudness_sensor) > 30:
                grovepi.digitalWrite(led, 1)  # Send HIGH to switch on LED
                print ("LED ON!")
                # Video capture
                camera.start_recording("/home/pi/" + date + ".h264")
                camera.wait_recording(10)
                camera.stop_recording()
                #Anfang theoretischer Code
                # eine Datei öffnen
                #1. Möglichkeit
                open file as startTcp:
                write( leg los mit dem TCP)
                close file
                #2. Möglichkeit
                Start(TCPClient)



                #Ende theoretischer Code
                time.sleep(1)
                grovepi.digitalWrite(led, 0)  # Send LOW to switch off LED

                # Image capture
                # camera.capture('/home/pi/Desktop/live2.jpg')
                # print("Image Shot")

            else:
                print '-'

            # if your hold time is less than this, you might not see as many detections
            time.sleep(1)

        except IOError as error:
print("Error in Surveillance " + error)rint("Error in Surveillance " + error)