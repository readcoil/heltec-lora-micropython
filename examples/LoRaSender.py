from time import sleep
from oled import *

def send(lora):
    counter = 0
    print("LoRa Sender")

    while True:
        payload = 'Hello ({0})'.format(counter)
        #print("Sending packet: \n{}\n".format(payload))
        lora.println(payload)

        counter += 1
        sleep(5)