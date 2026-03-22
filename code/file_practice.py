import time
import random

altitude = 310.0

with open('test_log.csv', 'w') as f:
    f.write('reading,altitude_m,temperature_c\n')
    
    for i in range(10):
        altitude = altitude + random.uniform(-0.5, 2.0)
        temperature = 22.0 + random.uniform(-0.2, 0.2)
        
        row = f"{i},{altitude:.2f},{temperature:.1f}\n"
        f.write(row)
        print(f"Wrote row {i}")
        
print("Done. File saved.")