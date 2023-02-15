import sys
import os
import time
import machine
import ubinascii

def mac2eui(mac):
    mac = f'{mac[:6]}fffe{mac[6:]}'
    return hex(int(mac[:2], 16) ^ 2)[2:] + mac[2:]

def get_millis():
    return time.ticks_ms()

def get_nodename():
    uuid = ubinascii.hexlify(machine.unique_id()).decode()
    return f"ESP_{uuid}"
