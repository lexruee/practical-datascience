#!/usr/bin/env python

from matplotlib import pyplot as plt
from collections import Counter
import random
import math


def median(xs):
    l = len(xs)
    xss = sorted(xs)
    m = l // 2
    if l % 2 == 0:
        lo = m -1
        hi = m
        return (xss[lo] + xss[hi])/2
    else:
        return xss[m]

def mean(xs):
    l = len(xs)
    mean_xs = sum(xs)/l
    return mean_xs

def de_mean(xs):
    mean_xs = mean(xs)
    return [(x - mean_xs) for x in xs]

def variance(xs):
    l = len(xs)
    ys = de_mean(xs)
    return sum([y**2 for y in ys])/(l-1)

def std(xs):
    variance_xs = variance(xs)
    return math.sqrt(variance_xs)


xs = [random.uniform(0, 100) for _ in range(0, 100)]

min_xs = min(xs)
max_xs = max(xs)
length = len(xs)
mean_xs = mean(xs)
variance_xs = variance(xs)
std_xs = std(xs)
median_xs = median(xs)


print("min: %s" % min_xs)
print("max: %s" % max_xs)
print("varaince: %s" % variance_xs)
print("std: %s" % std_xs)
print("length: %s" % length)
print("mean: %s" % mean_xs)
print("median: %s" % median_xs)
