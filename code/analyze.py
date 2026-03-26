import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read data
df = pd.read_csv('../data/simulated_flight.csv')

df['time_s'] = df['time_ms'] / 1000

df['total_g'] = np.sqrt(df['ax_g']**2 + df['ay_g']**2 + df['az_g']**2)

#interpret and print
print("FLIGHT SUMMARY")
print(f"Duration: {df['time_s'].max():.1f} seconds")
print(f"Max altitude: {df['altitude_m'].max():.2f} m")
print(f"Min altitude: {df['altitude_m'].min():.2f} m")
print(f"Max g-force: {df['total_g'].max():.3f} g")
print(f"Avg temperature: {df['temp_c'].mean():.1f} °C")

fig, axes = plt.subplots(3, 1, figsize=(12, 10))
fig.suptitle('Simulated Flight Analysis', fontsize=16, fontweight='bold')

#Altitude
axes[0].plot(df['time_s'], df['altitude_m'], color='#00cfff', linewidth=1.5)
axes[0].set_ylabel('Altitude (m)')
axes[0].set_title('Altitude vs Time')
axes[0].grid(True, alpha=0.3)

#Temp
axes[1].plot(df['time_s'], df['temp_c'], color='#ffcc00', linewidth=1.5)
axes[1].set_ylabel('Temperature (°C)')
axes[1].set_title('Temperature vs Time')
axes[1].grid(True, alpha=0.3)

#G-force
axes[2].plot(df['time_s'], df['total_g'], color='#39ff6e', linewidth=1.5)
axes[2].set_ylabel('Acceleration (g)')
axes[2].set_xlabel('Time (seconds)')
axes[2].set_title('Total G-Force vs Time')
axes[2].grid(True, alpha=0.3)
axes[2].axhline(y=1.0, color='red', linestyle='--', alpha=0.5, label='1g baseline')

plt.tight_layout()
plt.savefig('../data/flight_analysis.png', dpi=150, bbox_inches='tight')
plt.show()

print("Chart saved to data/flight_analysis.png")