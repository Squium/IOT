from machine import Pin, PWM
import utime
import random

led = PWM(Pin(1,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pinBtn = Pin(27, mode=Pin.IN, pull=Pin.PULL_UP)
lastDataBtn = 1
led.freq(1_000) # dont la frequence est de 1000 (default)
intens = 50000
led.duty_u16(0)
on = 1

while True:
    print(pinBtn.value())
    print(lastDataBtn)
    print("")
    if pinBtn.value() == 0 and lastDataBtn == 1:
        if on == 1:
            led.duty_u16(0)
            on = 0
        else :
            led.duty_u16(intens)
            on = 1
    lastDataBtn = pinBtn.value()
    utime.sleep(0.02)
    intens = random.randrange(0, 65000, 1) # on met une intensité aléatoire pour le prochain allumage
    print(intens)
    
#    if pinBtn.value() == 0 :
#        led.on()
#        utime.sleep(0.1)
#    else :
#        led.off()
#        utime.sleep(0.1)
    
    

            
