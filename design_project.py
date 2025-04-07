#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(115200);

  // Initialize I2C on default pins (SDA & SCL)
  Wire.begin(26, 25);  // SDA = GPIO 26, SCL = GPIO 25

  Serial.println("Initializing MPU6050...");

  if (!mpu.begin(MPU6050_ADDRESS_AD0_LOW)) {  // AD0 connected to GND
    Serial.println("MPU6050 not found!");
    while (1);
  }
  Serial.println("MPU6050 Connected!");
}

void loop() {
  mpu.update();

  Serial.print("Accelerometer: ");
  Serial.print(mpu.getAccX());
  Serial.print(", ");
  Serial.print(mpu.getAccY());
  Serial.print(", ");
  Serial.println(mpu.getAccZ());

  Serial.print("Gyroscope: ");
  Serial.print(mpu.getGyroX());
  Serial.print(", ");
  Serial.print(mpu.getGyroY());
  Serial.print(", ");
  Serial.println(mpu.getGyroZ());

  delay(1000);
}
