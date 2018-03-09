#!/usr/bin/env python

from matplotlib import pyplot as plt
from collections import Counter
import random
import stats

xs = [random.uniform(0, 100) for _ in range(0, 100)]
ys = [random.uniform(0, 100) for _ in range(0, 100)]

min_xs = min(xs)
max_xs = max(xs)
length = len(xs)
mean_xs = stats.mean(xs)
variance_xs = stats.variance(xs)
std_xs = stats.std(xs)
median_xs = stats.median(xs)
data_range_xs = stats.data_range(xs)

print("min: %s" % min_xs)
print("max: %s" % max_xs)
print("varaince: %s" % variance_xs)
print("std: %s" % std_xs)
print("length: %s" % length)
print("mean: %s" % mean_xs)
print("median: %s" % median_xs)
print("range: %s" % data_range_xs)


covariance_xsys = stats.covariance(xs, ys)
print("covariance: %s" % covariance_xsys)
