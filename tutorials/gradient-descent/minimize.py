#!/usr/bin/env python

import helper
import math
import random

def sum_of_squares_gradient(v):
    return [2 * vi for  vi in v]

def sum_of_squares(v):
    return sum(vi ** 2 for vi in v)

v = [random.randint(-10, 10) for i in range(3)]

v = helper.minimize_batch(sum_of_squares, sum_of_squares_gradient, v)

print("minimum v", v)
print("minimum value", sum_of_squares(v))
