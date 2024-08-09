import serial
import pyautogui
import pydirectinput
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

# Thresholds for detecting tilts
threshold_left = -3.5
threshold_right = 3.5
threshold_down = -3.5
threshold_double_down = -5
threshold_space = 3
threshold_double_space =5
                            
# Debounce time to prevent multiple rapid presses
debounce_time = 0.8  # seconds
debounce_time_back = 0.8   # seconds
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
            # pyautogui.press('left')
            pydirectinput.press('left')
            last_press_time['left'] = current_time
            print('left')
        
        # Detect right tilt
        elif dx > threshold_right and (current_time - last_press_time['right'] > debounce_time):
            # pyautogui.press('right')
            pydirectinput.press('right',_pause=False)
            last_press_time['right'] = current_time
            print('right')
        
        # Detect down tilt
        if dy < threshold_double_down and (current_time - last_press_time['down'] > debounce_time_back):
            # pyautogui.press('down')
            pydirectinput.press(['down', 'down'])
            last_press_time['down'] = current_time
            print('ddown')

        elif dy < threshold_down and (current_time - last_press_time['down'] > debounce_time_back):
            # pyautogui.press('s')   
            pydirectinput.press('down')    
            # pyautogui.press('s', presses=2, interval=0.1)
            last_press_time['down'] = current_time
            print('down')

        # Detect up tilt for space bar 
        elif dy > threshold_double_space and (current_time - last_press_time['space'] > debounce_time):
            # pyautogui.press('space')
            pydirectinput.press(['space','space'])
            last_press_time['space'] = current_time
            print('dspace')
        elif dy > threshold_space and (current_time - last_press_time['space'] > debounce_time):
            # pyautogui.press('space')
            pydirectinput.press('space')
            last_press_time['space'] = current_time
            print('space')
        
     