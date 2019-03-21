from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
yin=100
y = (yin, yin, 0) #Yellow
win = 200
b = (win,win,win) # White

smiley_face = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, b, b, y, y, b, b, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, y, y, b, b, y, y, y,
   y, y, y, y, y, y, y, y
]

frowning_face = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, b, b, y, y, b, b, y,
   y, y, y, y, y, y, y, y,
   y, y, y, b, b, y, y, y,
   y, y, b, y, y, b, y, y,
   y, b, y, y, y, y, b, y
]

while True:
   sense.set_pixels(smiley_face)
   sleep(3)
   sense.set_pixels(frowning_face)
   sleep(3)
