#!/usr/bin/env python

from matplotlib import pyplot as plt
from collections import Counter
import random
import helper

xs = [random.uniform(0, 100) for _ in range(0, 100)]
ys = [random.uniform(0, 100) for _ in range(0, 100)]

min_xs = min(xs)
max_xs = max(xs)
length = len(xs)
mean_xs = helper.mean(xs)
variance_xs = helper.variance(xs)
std_xs = helper.std(xs)
median_xs = helper.median(xs)
data_range_xs = helper.data_range(xs)

print("min: %s" % min_xs)
print("max: %s" % max_xs)
print("varaince: %s" % variance_xs)
print("std: %s" % std_xs)
print("length: %s" % length)
print("mean: %s" % mean_xs)
print("median: %s" % median_xs)
print("range: %s" % data_range_xs)


covariance_xsys = helper.covariance(xs, ys)
correlation_xsys = helper.correlation(xs, ys)
print("covariance: %s" % covariance_xsys)
print("correlation: %s" % correlation_xsys)
