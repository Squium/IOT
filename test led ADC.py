from machine import Pin, PWM, ADC
import utime
import random

led = PWM(Pin(1,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pinBtn = ADC(Pin(26, mode=Pin.IN))
lastDataBtn = 1
led.freq(1_000) # dont la frequence est de 1000 (default)
led.duty_u16(0)
on = 1

while True:
  #  print(pinBtn.read_u16())
 #   led.duty_u16(pinBtn.read_u16())
  #  utime.sleep(0.1)
  #  print(pinBtn.read_u16())

    wait = ((65535 - pinBtn.read_u16())/65535)
    
    led.duty_u16(0)
    utime.sleep(wait)
    led.duty_u16(60000)
    utime.sleep(wait)
    
#    if pinBtn.value() == 0 :
#        led.on()
#        utime.sleep(0.1)
#    else :
#        led.off()
#        utime.sleep(0.1)
    
    

            
