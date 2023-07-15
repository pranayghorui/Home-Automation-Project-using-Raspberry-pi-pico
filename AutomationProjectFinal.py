from machine import UART, Pin
import time
bt = UART(0,9600)
L1 = Pin(11,Pin.OUT)
L2 = Pin(12,Pin.OUT)
L3 = Pin(13,Pin.OUT)
L4 = Pin(14,Pin.OUT)

L1.value(1)
L2.value(1)
L3.value(1)
L4.value(1)

while True:
    
    br = bt.readline()
    print("pp=",br)
    if br is not None:
        if "ON1" in br:
            L1.value(0)
        elif "OFF1" in br:
            L1.value(1)
            
        elif "ON2" in br:
            L2.value(0)
        elif "OFF2" in br:
            L2.value(1)
        
        elif "ON3" in br:
            L3.value(0)
        elif "OFF3" in br:
            L3.value(1)
            
        elif "ON4" in br:
            L4.value(0)
        elif "OFF4" in br:
            L4.value(1)
    else:
        print("No Value")
    time.sleep(0.1)
