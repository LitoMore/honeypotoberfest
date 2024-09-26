#!/usr/bin/python3
import playsound
import random

__author__ = "akemmanuel & carlosmintfan"
__copyright__ = "Copyright (c) 2024 akemmanuel"
__license__ = "MIT"

def play():
    while True:
        z = random.randint(0, 3000000)
        if z == 4:
            playsound.playsound("bad.mp3")

play() 
