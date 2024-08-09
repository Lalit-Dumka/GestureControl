# Gesture-Controlled Glove Using MPU6050 and Arduino

Watch the video below to see the project in action:

[![Watch the video](/media/thumbnail.png)](/media/mouse_control.mp4)  
*Video: Demonstration of the gesture-controlled glove.*

![Project Image](/media/setup.jpg)  
*Image: MPU and Arduino*

## Overview

This project demonstrates the creation of a gesture-controlled glove using the MPU6050 sensor and Arduino. Originally aimed at understanding the working of the MPU6050, this project evolved into a functional prototype that can control the Asphalt 9 car racing game and even the mouse pointer on a computer using simple hand gestures.

### Features

- **Game Controller**: The glove can control the steering and acceleration in Asphalt Unite.
- **Mouse Controller**: Move the mouse pointer with hand gestures.
- **Potential Applications**: Drone navigation, robotics control, and smart home automation, etc.

## How It Works

The core of this project is the MPU6050 sensor, a 6-axis motion tracking device that combines a 3-axis accelerometer and a 3-axis gyroscope. Here's how it works:

1. **Accelerometer**: Detects the glove's orientation in 3D space.
2. **Gyroscope**: Measures the glove's rotational movements.
3. **Data Processing**: The sensor data is processed by an Arduino microcontroller, which interprets the gestures and sends appropriate control signals to the connected device.



## Getting Started

### Requirements

- Arduino Uno
- MPU6050 Sensor
- Glove
- Wires and connectors
- Arduino IDE

### Setup Instructions

1. **Connect the MPU6050 to Arduino**: Follow this wiring:
    - VCC to 5V
    - GND to GND
    - SDA to A4
    - SCL to A5
2. **Upload the Code**: Use the Arduino IDE to upload the code to the Arduino board.
3. **Wear the Glove**: Attach the sensor to the glove and wear it.
4. **Run the Demo**: Use the glove to control the game or the mouse pointer.

### Code

The code for this project can be found in the `src` folder of this repository. Upload the `\arduino\mpu_6050_output\mpu_6050_output.ino` to arduino. Then run the python scripts inside the src folder.

## Applications

This project can be extended to several real-world applications:

- **Drone Navigation**: Control drones with intuitive hand gestures.
- **Robotics Control**: Operate robots remotely using gestures.
- **Smart Home Automation**: Manage smart home devices with simple hand movements.
- Other practical uses like 𝐩𝐫𝐨𝐬𝐭𝐡𝐞𝐭𝐢𝐜𝐬, 𝐀𝐃𝐀𝐒, 𝐕𝐑, 𝐖𝐞𝐚𝐫𝐚𝐛𝐥𝐞 𝐇𝐞𝐚𝐥𝐭𝐡 𝐌𝐨𝐧𝐢𝐭𝐨𝐫𝐬, etc.

## Future Work

- **Improved Accuracy**: Implement advanced filtering algorithms to enhance motion detection accuracy.
- **Additional Gestures**: Add more complex gestures for varied controls.
- **Wireless Communication**: Integrate Bluetooth or Wi-Fi for wireless operation.

## Contributions

Feel free to contribute to this project by opening issues or submitting pull requests. Any enhancements or additional features are welcome!

## LinkedIn post

[![LinkedIn Post](/media/linkedIn_thumbnail.png)](https://www.linkedin.com/posts/lalit-dumka_arduino-mpu6050-gesturecontrol-activity-7227635752560386048-14Ho?utm_source=share&utm_medium=member_desktop)
