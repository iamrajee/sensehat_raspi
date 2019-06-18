#!/usr/bin/python
import sys
import time
from sense_hat import SenseHat

X = (255, 0, 0)
O = (0, 0, 0)

question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, X, X, X, X, O, O,
    O, X, O, X, X, O, X, O,
    X, O, O, X, X, O, O, X,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O
]

sense = SenseHat()
sense.set_pixels(question_mark)

def arrow(dir):
	if dir == "L":
		sense.set_rotation(0)
	elif dir == "F":
                sense.set_rotation(90)
	elif dir == "R":
                sense.set_rotation(180)
	elif dir == "B":
                sense.set_rotation(270)
	time.sleep(5)
try:
	arrow("F")
	arrow("L")
        arrow("R")
        arrow("B")
except:
    sense.clear()
