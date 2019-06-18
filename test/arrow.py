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

try:
    while True:
        for r in [0, 90, 180, 270]:
            sense.set_rotation(r)
            time.sleep(1.0)
except:
    sense.clear()
