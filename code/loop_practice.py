import time
import random

counter = 0
altitude = 310.0

while True:
    counter = counter + 1
    altitude = altitude + random.uniform(-0.5, 2.0)
    temperature = 22.0 + random.uniform(-0.2, 0.2)
    az = 1.0 + random.uniform(-0.05, 0.05)
    

    print(f"Reading {counter} | Alt: {altitude:.2f}m | Temp: {temperature:.1f}*C | Az: {az:.3f}g")
    time.sleep(1)