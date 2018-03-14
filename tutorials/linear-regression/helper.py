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

def sols(ys, xs):
    beta = correlation(ys, xs) * std(ys) / std(xs)
    alpha = mean(ys) - beta * mean(xs)
    return alpha, beta

def ols(y, X, const=True):
    y = np.array([y]).transpose()
    ones = np.ones(y.shape)
    X = np.array(X).transpose() 
    X = np.hstack([X, ones])
    Xp = X.transpose()
    beta = np.linalg.inv(Xp.dot(X)).dot(Xp).dot(y)
    yp = X.dot(beta)
    u = y - yp
    return beta, yp, u
