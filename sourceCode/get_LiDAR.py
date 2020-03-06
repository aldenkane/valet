# Improvements
    # Return a flag that says whether or not a distance was picked up
    # Get this to not be so buggy

import smbus

def get_LiDAR():
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

    # Read the STATUS Register
    r_1 = bus.read_byte_data(DEVICE_ADDRESS, STATUS)

    # Check to see if distance can be read from device
    if r_1 == 1:
        try:
            read_Distance_0 = bus.read_byte_data(DEVICE_ADDRESS, FULL_DELAY_LOW)
            read_Distance_1 = bus.read_i2c_block_data(DEVICE_ADDRESS, FULL_DELAY_LOW, 2)
        except:
            read_Distance_0 = 'Null - No Signal Acquired'
    else:
        pass

    return read_Distance_0