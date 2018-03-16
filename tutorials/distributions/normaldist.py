#!/usr/bin/env python

from matplotlib import pyplot as plt
import math

def normal_pdf(x, mu=0, sigma=1):
    factor = 1/math.sqrt((2*math.pi*sigma))
    v = -1 * ((x-mu)**2)/(2*sigma**2)
    return factor * math.exp(v)

xs = [x/10 for x in range(-50, 50)]
ys1 = [normal_pdf(x, 0, 1) for x in xs]
ys2 = [normal_pdf(x, 0, 2) for x in xs]
ys3 = [normal_pdf(x, 0, 0.5) for x in xs]
ys4 = [normal_pdf(x, -1, 1) for x in xs]


plt.plot(xs, ys1, 'b--')
plt.plot(xs, ys2, 'r--')
plt.plot(xs, ys3, 'g--')
plt.plot(xs, ys4, 'k--')
plt.title('Various Normal Distributions')
plt.ylabel('f(x)')
plt.xlabel('Value')
plt.legend(['N(mu=0,sigma=1)', 'N(mu=0,sigma=2)', 'N(mu=0,sigma=0.5)', 
    'N(mu=-1,sigma=1'])
plt.show()

