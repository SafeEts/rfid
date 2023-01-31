import RPi.GPIO as GPIO
import time

from pkg_resources import _initialize


class brila():
    def __init__(self):
        self.LED_PIN_RED = 26
        self.LED_PIN_GREEN = 16
        # self.porta = 12
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_PIN_RED, GPIO.OUT)
        GPIO.setup(self.LED_PIN_GREEN, GPIO.OUT)
        # GPIO.setup(self.porta, GPIO.OUT)
    def onGreen(self):
        GPIO.output(self.LED_PIN_GREEN, GPIO.HIGH)
    def onRed(self):
        GPIO.output(self.LED_PIN_RED, GPIO.HIGH)
    def offRed(self):
        GPIO.output(self.LED_PIN_RED, GPIO.LOW)
    def offGreen(self):
        GPIO.output(self.LED_PIN_GREEN, GPIO.LOW)
    def abrir(self):
        self.porta = 12
        GPIO.setup(self.porta, GPIO.OUT)
        GPIO.output(self.porta, 0)
    def fechar(self):
        GPIO.cleanup(12)
    def finish(self):
        GPIO.cleanup()



