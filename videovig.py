import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)
estado_alarma = False
time.sleep(2)
print('ALARMA OFF')
    
def comprobarEstado(estado_previo):
    estado_actual = GPIO.input(4)
    if estado_actual != estado_previo:
        if estado_actual:
            print('ALARMA ON')
        else:
            print('ALARMA OFF')      
    return estado_actual


while True:
    time.sleep(0.5)
    estado_alarma = comprobarEstado(estado_alarma)

    while estado_alarma:
        os.system("fswebcam -i 0 -d /dev/video0 -r 640x480 -p YUYV -q --title @GMSVideoVig  /var/www/html/images/%d%m%y_%H%M%S.jpg")
        time.sleep(0.5)
        estado_alarma = comprobarEstado(estado_alarma)
