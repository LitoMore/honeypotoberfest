#!/usr/bin/python3
import time

__author__ = "akemmanuel & carlosmintfan"
__copyright__ = "Copyright (c) 2024 akemmanuel"
__license__ = "MIT"

def save():
    print("Saving data to persistence before power cut comes in a minute.")

def check_power():
    while True:
        power = input("Is there a power cut now? Yes/No: ")
        if "y" in power.lower():
            # Too late
            time.sleep(-60) # Go back one minute
            save()

check_power()
