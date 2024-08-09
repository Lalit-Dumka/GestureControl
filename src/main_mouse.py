import serial
import pyautogui
import time

# Configure serial port
ser = serial.Serial('COM10', 115200)  # Replace 'COM3' with your serial port

# Calibrate initial accelerometer readings to prevent abrupt mouse movements
initial_readings = None

def get_acceleration_data():
    line = ser.readline().decode('utf-8').strip()
    try:
        x, y, z = map(float, line.split(','))
        return x, y, z
    except ValueError:
        return None

# Mouse movement sensitivity
sensitivity = 10

while True:
    data = get_acceleration_data()
    print(data)
    if data:
        x, y, z = data
        
        # Initialize initial readings
        if initial_readings is None:
            initial_readings = (x, y, z)
        
        # Calculate movement based on difference from initial readings
        dx = (x - initial_readings[0]) * sensitivity
        dy = (y - initial_readings[1]) * sensitivity
        
        # Move the mouse cursor
        pyautogui.moveRel(dx, -dy)
        
    # time.sleep(0.1)  # Adjust the delay as necessary
