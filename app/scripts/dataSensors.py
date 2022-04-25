import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from gpiozero import MotionSensor

class dataSensors:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)


    def us(self, pin1, pin2):
        GPIO_ECHO = pin1
        GPIO_TRIGGER = pin2
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)
        GPIO.output(GPIO_TRIGGER, True)
        GPIO.output(GPIO_TRIGGER, False)
        StartTime = time.time()
        StopTime = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
        TimeElapsed = StopTime - StartTime
        distancia = (TimeElapsed * 34300) / 2
        return distancia
    
    def th(self, pin):
        sensor = Adafruit_DHT.DHT11
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        return [temperatura, humedad]

    def pir(self, pin):
        GPIO_PIR = pin
        GPIO.setup(GPIO_PIR, GPIO.IN)
        if GPIO.input(GPIO_PIR):
            led = 4
            GPIO.setup(led, GPIO.OUT)
            pir = MotionSensor(pin)
            pir.wait_for_motion()
            mensaje = 'Se ha detectado presencia'
            GPIO.output(led, True)
            pir.wait_for_no_motion()
            GPIO.output(led, False)
            return mensaje
        else:
            return 'No se ha detectado presencia'
    
    def gh(self, pin1, pin2):
        GPIO.setup(pin1, GPIO.IN)
        GPIO.setup(pin2, GPIO.OUT)
        if GPIO.input(pin1):
            return 'No se ha detectado nada'
        elif GPIO.input(pin1) != 1:
            buzzer = 26
            GPIO.setup(buzzer, GPIO.OUT)
            GPIO.output(buzzer, True)
            GPIO.output(pin2, False)
            time.sleep(1)
            GPIO.output(pin2, True)
            GPIO.output(buzzer, False)
            hg = 'Se ha detectado algo'
            return hg

