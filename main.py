# File: main.py

from bmw import BMW
from audi import Audi
from nissan import Nissan

# Create car objects
bmw_car = BMW("X5")
audi_car = Audi("A4")
nissan_car = Nissan("Altima")

# Display car information
bmw_car.display_info()
audi_car.display_info()
nissan_car.display_info()

# Perform car-specific functionality
bmw_car.start_engine()
audi_car.stop_engine()
nissan_car.accelerate()
