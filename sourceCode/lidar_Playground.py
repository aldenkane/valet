import smbus

# Declare Globals and Device Parameters
CHANNEL = 1
DEVICE_ADDRESS = 0x62
DISTANCE_LOW_BYTE = 0x10
DISTANCE_HIGH_BYTE = 0X11
RESET_BYTE = 0x00

# Declare Bus w/ SMbus
bus = smbus.SMBus(CHANNEL)

#Reset Measurements
bus.write_byte_data(DEVICE_ADDRESS, DISTANCE_LOW_BYTE, RESET_BYTE)
bus.write_byte_data(DEVICE_ADDRESS, DISTANCE_HIGH_BYTE, RESET_BYTE)

#Read device data
low_Distance = bus.read_byte_data(DEVICE_ADDRESS, DISTANCE_LOW_BYTE)
high_Distance = bus.read_byte_data(DEVICE_ADDRESS, DISTANCE_HIGH_BYTE)

print("Low Distance Byte: " + str(low_Distance) + " cm")
print("Low Distance Byte: " + str(high_Distance) + " cm")