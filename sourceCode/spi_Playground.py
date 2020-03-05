# spi_Playground

import time
import spidev

# Initialize Globals
bus = 0
device = 1

#Enable SPI
spi = spidev.Spidev()

# Open a