from machine import Pin, PWM
import utime
import random

ledB = PWM(Pin(19,mode=Pin.OUT))
ledG = PWM(Pin(18,mode=Pin.OUT))
ledR = PWM(Pin(17,mode=Pin.OUT)) # on prescise au programme que les pin 17, 18, 19 sont des sorties de type PWN

couleur = [255, 255, 255]

ledR.freq(1_000) # dont la frequence est de 1000 (default)
ledG.freq(1_000) # dont la frequence est de 1000 (default)
ledB.freq(1_000) # dont la frequence est de 1000 (default)


while True:
    
    ledR.duty_u16(couleur[0] * 257)
    print("Rouge = ")
    print(couleur[0])
    ledG.duty_u16(couleur[1] * 257)
    print("Vert = ")
    print(couleur[1])
    ledB.duty_u16(couleur[2] * 257)
    print("Bleu = ")
    print(couleur[2])
    utime.sleep(0.05)