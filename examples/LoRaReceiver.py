from oled import *

def receive(lora):
    oled, screen = init_oled()

    print("LoRa Receiver")

    while True:
        if lora.received_packet():
            lora.blink_led()
            print('something here')
            payload = lora.read_payload()
            print(payload)
            screen[0] = f"pkt: {payload}"
            write_screen(oled, screen)

