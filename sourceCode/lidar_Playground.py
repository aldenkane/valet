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
bus = smbus.SMBus(CHANNEL)

# Initialize LiDAR by Writing to Correction Distance Mode to ACQ Register
bus.write_byte_data(DEVICE_ADDRESS, ACQ_COMMANDS, BIASED_DISTANCE)

# Read Distance Data
r_1 = bus.read_byte_data(DEVICE_ADDRESS, STATUS)
r_1_Bin = bin(r_1)

print("Read Status Distance: " + str(r_1) + 'cm')
