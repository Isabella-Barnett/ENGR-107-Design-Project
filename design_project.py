# https://github.com/varnicm/mpu6050-interface/blob/main/mpu6050_script.py
# TODO: modify this example script

import smbus
import time

# Class for interfacing with the MPU6050
class MPU6050:
    def __init__(self):
        self.bus = smbus.SMBus(1)  # or SMBus(0) on older Raspberry Pi's
        self.device_address = 0x68  # MPU6050 device address

        # Wake up the MPU6050 as it starts in sleep mode
        self.bus.write_byte_data(self.device_address, 0x6B, 0)

    def read_raw_data(self, addr):
        # Read raw 16-bit value
        high = self.bus.read_byte_data(self.device_address, addr)
        low = self.bus.read_byte_data(self.device_address, addr + 1)

        # Concatenate higher and lower value
        value = ((high << 8) | low)

        # To get signed value from mpu6050
        if value > 32768:
            value = value - 65536
        return value

    def get_accel_data(self):
        # Read accelerometer data
        acc_x = self.read_raw_data(0x3B)
        acc_y = self.read_raw_data(0x3D)
        acc_z = self.read_raw_data(0x3F)

        return {'x': acc_x, 'y': acc_y, 'z': acc_z}

# Create MPU6050 instance
mpu = MPU6050()

# Loop to continuously get data
try:
    while True:
        accel_data = mpu.get_accel_data()
        print(f"Accel Data: X:{accel_data['x']}, Y:{accel_data['y']}, Z:{accel_data['z']}")
        time.sleep(1)  # Delay of 1 second

except KeyboardInterrupt:
    print("Interrupted by user")