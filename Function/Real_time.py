import time
import random

def fetch_sensor_data():
    """Simulate reading sensor data."""
    return random.uniform(20.0, 30.0)  # Temperature in °C

# Real-time loop
while True:
    temperature = fetch_sensor_data()
    print(f"Temperature: {temperature:.2f} °C")
    time.sleep(1)  # Wait 1 second before next reading
