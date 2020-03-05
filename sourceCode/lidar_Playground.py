import smbus

# Declare Globals and Device Parameters
CHANNEL = 1
DEVICE_ADDRESS = 0x62
ACQ_COMMANDS = 0x00
FULL_DELAY_LOW = 0x10
FULL_DELAY_HIGH = 0X11
RESET_BYTE = 0x00
BIASED_DISTANCE = 0X00

# Declare Bus w/ SMbus
bus = smbus.SMBus(CHANNEL)

# Write Distance Command w/ Receiver Correction
bus.write_byte_data(DEVICE_ADDRESS, ACQ_COMMANDS, BIASED_DISTANCE)

#Reset Measurements
bus.write_byte_data(DEVICE_ADDRESS, FULL_DELAY_LOW, RESET_BYTE)
bus.write_byte_data(DEVICE_ADDRESS, FULL_DELAY_HIGH, RESET_BYTE)

#Read device data
low_Distance = bus.read_byte_data(DEVICE_ADDRESS, FULL_DELAY_LOW)
high_Distance = bus.read_byte_data(DEVICE_ADDRESS, FULL_DELAY_HIGH)

print("Low Distance Byte: " + str(low_Distance) + " cm")
print("Low Distance Byte: " + str(high_Distance) + " cm")