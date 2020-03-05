import smbus

# Declare Globals and Device Parameters
CHANNEL = 1
DEVICE_ADDRESS = 0x62

ACQ_COMMANDS = 0x00
STATUS = 0x01
FULL_DELAY_LOW = 0x10
FULL_DELAY_HIGH = 0X11

RESET_BYTE = 0x00
BIASED_DISTANCE = 0X04


# Declare Bus w/ SMbus, Intialize I2C
bus = smbus.SMBus(CHANNEL, STATUS)

# Initialize LiDAR by Writing to Correction Distance Mode to ACQ Register
bus.write_byte_data(DEVICE_ADDRESS, ACQ_COMMANDS, BIASED_DISTANCE)

# Read Distance Data
r_Stat = bus.read_byte_data(DEVICE_ADDRESS, STATUS)

#Reset Measurements
bus.write_byte_data(DEVICE_ADDRESS, FULL_DELAY_LOW, RESET_BYTE)
bus.write_byte_data(DEVICE_ADDRESS, FULL_DELAY_HIGH, RESET_BYTE)

#Read device data
low_Distance = bus.read_byte_data(DEVICE_ADDRESS, FULL_DELAY_LOW)
high_Distance = bus.read_byte_data(DEVICE_ADDRESS, FULL_DELAY_HIGH)

print("Read Status Distance: " + str(r_Stat) + 'cm')
print("Low Distance Byte: " + str(low_Distance) + " cm")
print("Low Distance Byte: " + str(high_Distance) + " cm")