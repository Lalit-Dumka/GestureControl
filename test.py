import serial
import pyautogui
import time

# Configure serial port
ser = serial.Serial('COM10', 115200)  # Replace 'COM10' with your serial port

# Calibrate initial accelerometer readings to prevent abrupt mouse movements
initial_readings = None

def get_acceleration_data():
    line = ser.readline().decode('utf-8').strip()
    try:
        x, y, z = map(float, line.split(','))
        return x, y, z
    except ValueError:
        return None

def double_tap(key, interval=0.1):
    """Function to double tap a key with a specified interval."""
    pyautogui.press(key)
    time.sleep(interval)
    pyautogui.press(key)

# Thresholds for detecting tilts
threshold_left = -3.5
threshold_right = 3.5
threshold_down = -3.5
threshold_space = 3.0

# Debounce time to prevent multiple rapid presses
debounce_time = 0.2  # seconds
last_press_time = {
    'left': 0,
    'right': 0,
    'down': 0,
    'space': 0
}

while True:
    data = get_acceleration_data()
    if data:
        x, y, z = data
        
        # Initialize initial readings
        if initial_readings is None:
            initial_readings = (x, y, z)
        
        # Calculate movement based on difference from initial readings
        dx = x - initial_readings[0]
        dy = y - initial_readings[1]
        
        current_time = time.time()

        # Detect left tilt
        if dx < threshold_left and (current_time - last_press_time['left'] > debounce_time):
            pyautogui.press('left')
            last_press_time['left'] = current_time
            print('left')
        
        # Detect right tilt
        elif dx > threshold_right and (current_time - last_press_time['right'] > debounce_time):
            pyautogui.press('right')
            last_press_time['right'] = current_time
            print('right')
        
        # Detect down tilt for 360 spin
        if dy < threshold_down and (current_time - last_press_time['down'] > debounce_time):
            double_tap('s', interval=0.1)
            last_press_time['down'] = current_time
            print('down 360')

        # Detect up tilt for space bar (e.g., jumping in a game)
        elif dy > threshold_space and (current_time - last_press_time['space'] > debounce_time):
            pyautogui.press('space')
            last_press_time['space'] = current_time
            print('space')
        
    # time.sleep(0.01)  # Adjust the delay as necessary
