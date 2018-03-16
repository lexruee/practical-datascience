#!/usr/bin/env python

from matplotlib import pyplot as plt
import math

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

xs = [x/10 for x in range(-50, 50)]
ys1 = [normal_cdf(x, 0, 1) for x in xs]
ys2 = [normal_cdf(x, 0, 2) for x in xs]
ys3 = [normal_cdf(x, 0, 0.5) for x in xs]
ys4 = [normal_cdf(x, -1, 1) for x in xs]


plt.plot(xs, ys1, 'b--')
plt.plot(xs, ys2, 'r--')
plt.plot(xs, ys3, 'g--')
plt.plot(xs, ys4, 'k--')
plt.title('Various Cumulative Normal Distributions')
plt.ylabel('f(x)')
plt.xlabel('Value')
plt.legend(['Erf(mu=0,sigma=1)', 'Erf(mu=0,sigma=2)', 'Erf(mu=0,sigma=0.5)', 
    'Erf(mu=-1,sigma=1'])
plt.show()

