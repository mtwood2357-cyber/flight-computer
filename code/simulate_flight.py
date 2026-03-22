import random
import csv

#flight parameters
launch_altitude = 310.0
max_altitude = 460.0
current_altitude = launch_altitude

with open('../data/simulated_flight.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    
    #header
    writer.writerow(['time_ms', 'altitude_m', 'temp_c', 'pressure_hpa', 'ax_g', 'ay_g', 'az_g'])
    
    #launch
    for i in range(6):
        t = i * 500
        current_altitude += random.uniform(8.0, 12.0)
        temp = 22.0 + random.uniform(-0.2, 0.2)
        pressure = 977.0 - (current_altitude - launch_altitude) * 0.12
        ax = random.uniform(-0.3, 0.3)
        ay = random.uniform(-0.3, 0.3)
        az = random.uniform(4.0, 8.0)
        writer.writerow([t, round(current_altitude,3), round(temp,2), round(pressure,2), round(ax,4), round(ay,4), round(az,4)])
        
    #coast
    for i in range(14):
        t = (i + 6) * 500
        current_altitude += random.uniform(1.0, 6.0)
        temp = 22.0 + random.uniform(-0.5, 0.5)
        pressure = 977.0 - (current_altitude - launch_altitude) * 0.12
        ax = random.uniform(-0.1, 0.1)
        ay = random.uniform(-0.1, 0.1)
        az = random.uniform(0.8, 1.2)
        writer.writerow([t, round(current_altitude,3), round(temp,2), round(pressure,2), round(ax,4), round(ay,4), round(az,4)])
    
    #decent
    for i in range(20):
        t = (i + 20) * 500
        current_altitude -= random.uniform(3.0, 7.0)
        if current_altitude < launch_altitude:
            current_altitude = launch_altitude
        temp = 22.0 + random.uniform(-0.2, 0.2)
        pressure = 977.0 - (current_altitude - launch_altitude) * 0.12
        ax = random.uniform(-0.2, 0.2)
        ay = random.uniform(-0.2, 0.2)
        az = random.uniform(0.9, 1.1)
        writer.writerow([t, round(current_altitude,3), round(temp,2), round(pressure,2), round(ax,4), round(ay,4), round(az,4)])

print("Simulated flight data written to data/simulated_flight.csv")