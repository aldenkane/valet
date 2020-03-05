import smbus

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x62      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
distance_Low_Byte = 0x10
DEVICE_REG_LEDOUT0 = 0x1d

#Read device data

read = bus.read_block_data(DEVICE_ADDRESS, distance_Low_Byte, 0x01)

print(read)