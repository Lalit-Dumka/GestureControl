#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  
  if (mpu.testConnection()) {
    Serial.println("MPU6050 connection successful");
  } else {
    Serial.println("MPU6050 connection failed");
  }
}

void loop() {
  int16_t ax, ay, az;
  int16_t gx, gy, gz;
  
  // Read accelerometer and gyroscope data
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  
  // Determine the direction of linear movement based on accelerometer data
  if (ax > 10000) {
    Serial.println("Moving Right");
  } else if (ax < -10000) {
    Serial.println("Moving Left");
  }

  if (ay > 10000) {
    Serial.println("Moving Up");
  } else if (ay < -10000) {
    Serial.println("Moving Down");
  }

  // if (az > 10000) {
  //   Serial.println("Moving Forward");
  // } else if (az < -10000) {
  //   Serial.println("Moving Backward");
  // }

  // Determine the direction of rotational movement based on gyroscope data
  if (gx > 5000) {
    Serial.println("Rotating Right");
  } else if (gx < -5000) {
    Serial.println("Rotating Left");
  }

  if (gy > 5000) {
    Serial.println("Rotating Up");
  } else if (gy < -5000) {
    Serial.println("Rotating Down");
  }

  if (gz > 5000) {
    Serial.println("Rotating Clockwise");
  } else if (gz < -5000) {
    Serial.println("Rotating Counterclockwise");
  }
  
  delay(100); // Adjust the delay as necessary
}
