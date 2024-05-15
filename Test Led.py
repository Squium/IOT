from machine import Pin 
import utime 

led = Pin(1, mode=Pin.OUT)
led2 = Pin(5, mode=Pin.OUT)
led3 = Pin(9, mode=Pin.OUT)
led4 = Pin(14, mode=Pin.OUT)
wait = 0.2


while True:
    led.on()
    utime.sleep(wait)
    led.off()
    led2.on()
    utime.sleep(wait)
    led2.off()
    led3.on()
    utime.sleep(wait)
    led3.off()
    led4.on()
    utime.sleep(wait)
    led4.off()
    led3.on()
    utime.sleep(wait)
    led3.off()
    led2.on()
    utime.sleep(wait)
    led2.off()
    

 