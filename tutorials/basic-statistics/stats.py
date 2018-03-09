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

def covariance(xs, ys):
    l = len(xs)
    xss, yss = de_mean(xs), de_mean(ys)
    return sum([x * y for x,y in zip(xss, yss)])/(l-1)

