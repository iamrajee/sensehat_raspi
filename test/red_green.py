from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

rin=255
r = (rin, 0, 0) #red
gin = 255
g = (0, gin, 0) #green

def red():
	sense.set_pixels([r for i in range(64)])
def green():
        sense.set_pixels([g for i in range(64)])

try:
	while True:
		red()
		sleep(1)
		green()
		sleep(1)
except:
	sense.clear()
