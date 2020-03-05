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

read_Distance = 0

# Declare Bus w/ SMbus, Intialize I2C
bus = smbus.SMBus(CHANNEL)

# Initialize LiDAR by Writing to Correction Distance Mode to ACQ Register
bus.write_byte_data(DEVICE_ADDRESS, ACQ_COMMANDS, BIASED_DISTANCE)

r_1 = bus.read_byte_data(DEVICE_ADDRESS, STATUS)
if r_1 == 1:
    read_Distance_0 = bus.read_byte_data(DEVICE_ADDRESS, FULL_DELAY_LOW)
    read_Distance_1 = bus.read_i2c_block_data(DEVICE_ADDRESS, FULL_DELAY_LOW, 2)
    print("Read Distance " + str(read_Distance_0) + ' cm')
    exit()



