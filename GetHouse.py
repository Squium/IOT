import network   #import des fonctions liées au wifi
import urequests    #import des fonctions liées aux requetes http
import utime    #import des fonctions liées au temps
import ujson    #import des fonctions liées à la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time # importe dans le code la lib qui permet de gerer le temps

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'HUAWEI P30'
password = 'Poulet2005$'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://10.2.164.29:3000/houses"

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    print("co")
    leds = [PWM(Pin(19, mode = Pin.OUT)), PWM(Pin(18, mode = Pin.OUT)), PWM(Pin(17, mode = Pin.OUT))]
        
    houses = {
        "Gryffindor" : [255,0,0],
        "Slytherin" : [0,255,0],
        "Ravenclaw" : [0,0,255],
        "Hufflepuff" : [255,255,0]
    }
        
    #characters = ["harry-potter", "draco-malfoy", "luna-lovegood", "cedric-diggory"]
        
    #for c in characters :
    r = urequests.get(url)
    utime.sleep(0.1)
    print(r.json()["house"])
        

    for i in leds :
        i.freq(1_000)
        i.duty_u16(0)

    def setColor (house) :
        for i in range(3):
            leds[i].duty_u16(house[i]*256)
        print(r.json()["house"])

    setColor(houses[r.json()["house"]])
    