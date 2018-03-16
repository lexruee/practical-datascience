#!/usr/bin/env python

import helper
import math
import random

def step(v, direction, step_size):
    return [vi  + step_size * direction_i for vi, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * vi for  vi in v]

def distance(v, w):
    return math.sqrt(sum((vi - wi)**2 for vi, wi in zip(v, w)))

v = [random.randint(-10, 10) for i in range(3)]
tolerance = 0.000001

while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v

print(v)
