#!/usr/bin/env python
import time
# import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

from outro import brila

light = brila()
# LED_PIN_RED = 26
# LED_PIN_GREEN = 16
# GPIO.cleanup()
reader = SimpleMFRC522()
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LED_PIN_RED, GPIO.OUT)
# GPIO.setup(LED_PIN_GREEN, GPIO.OUT)
while True:
    light.offRed()
    light.offGreen()
    # GPIO.output(LED_PIN_RED, GPIO.LOW)
    # GPIO.output(LED_PIN_GREEN, GPIO.LOW)
    try:
        text = input('New data:')
        if text == "":
            break

        if text != "508430":
            # GPIO.output(LED_PIN_RED, GPIO.HIGH)
            print("\nYou don't have permission!\n")
            # ACENDE UM LED DE ERRO
            light.onRed()
            time.sleep(3)
            continue

        # ACENDE UM LED DE SUCESSO
        light.onGreen()
        light.abrir()
        # GPIO.output(LED_PIN_GREEN, GPIO.HIGH)
        print("Now place your tag to write")
        a = reader.write(text)

        tagID = a[0]
        cardID = a[1]
        print("Tag ID: ", tagID)
        print("Card ID: ",cardID)
        print(type(a))
        print("Saved")
        light.fechar()
    finally:
        print("NEXT ======")
# light.finish()
GPIO.cleanup()