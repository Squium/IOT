from machine import Pin 
import utime

led = Pin(1, mode=Pin.OUT)
pinBtn = Pin(27, mode=Pin.IN, pull=Pin.PULL_UP)
lastDataBtn = 1

while True:
    print(pinBtn.value())
    print(lastDataBtn)
    print("")
    if pinBtn.value() == 0 and lastDataBtn == 1:
        led.toggle()
    lastDataBtn = pinBtn.value()
    utime.sleep(0.1)
    
#    if pinBtn.value() == 0 :
#        led.on()
#        utime.sleep(0.1)
#    else :
#        led.off()
#        utime.sleep(0.1)
    
    

            
