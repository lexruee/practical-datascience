import math
import numpy as np

def data_range(xs):
    return max(xs) - min(xs)

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

def correlation(xs, ys):
    sx, sy = std(xs), std(ys)
    sxy = covariance(xs, ys)
    if sx and sy:
        return sxy / (sx * sy)
    else:
        return 0

def difference_quotient(f, x, h):
    return (f(x + h) - f(x))/h

def partial_difference_quotient(f, v, i, h):
    w = [vj + (h if j == i else 0) for j, vj in enumerate(v)]
    return (f(w) - f(v))/ h

def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h) for i,_ in enumerate(v)]

def step(v, direction, step_size):
    return [vi  + step_size * direction_i for vi, direction_i in zip(v,
        direction)]

def sum_of_squares_gradient(v):
    return [2 * vi for  vi in v]

def distance(v, w):
    return math.sqrt(sum((vi - wi)**2 for vi, wi in zip(v, w)))

def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0                           # set theta to initial value
    target_fn = safe(target_fn)               # safe version of target_fn
    value = target_fn(theta)                  # value we're minimizing

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]

        # choose the one that minimizes the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        # stop if we're "converging"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value

