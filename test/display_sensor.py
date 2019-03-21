from sense_hat import SenseHat
sense = SenseHat()
while (1):
	sense.show_message("T="+str(sense.get_temperature()).split(".")[0])
	sense.show_message("P="+str(sense.get_pressure()).split(".")[0])
	sense.show_message("H="+str(sense.get_humidity()).split(".")[0])
