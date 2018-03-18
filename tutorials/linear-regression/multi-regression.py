#!/usr/bin/env python

from matplotlib import pyplot as plt
import helper
import csv
import math
import sys
import numpy as np

y, X = [], []
gest, weight, length, smoking = [], [], [], []

with open('../infants-smoke.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        gest.append(float(row['Gest']))
        weight.append(float(row['Weight']))
        length.append(float(row['Length']))
        smoking.append(1 if row['Smoking'] == 'YES' else 0)

X = [smoking, gest, length]
y = weight[:]

beta, yp, u  = helper.ols(y, X, const=True)

print("beta: %s" % beta)

sq_errors = [e * e for e in u]
sse = np.sum(sq_errors)
tss = sum([ y * y for y in helper.de_mean(y)])
r_sq = 1.0 - sse / tss 
print("r-squared: %s " % r_sq)


plt.plot(range(len(y)), y, '-bo', range(len(y)), yp, '-ro')
plt.title('Actual vs Predicted')
plt.xlabel('Obs')
plt.ylabel('Grams')
plt.legend(['Actual', 'Predicted'])
plt.grid()
plt.show()
