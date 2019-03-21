from sense_hat import SenseHat
sense = SenseHat()
print("T=",sense.get_temperature())
print("P=",sense.get_pressure())
print("H=",sense.get_humidity())
