#!/usr/bin/env python

from matplotlib import pyplot as plt
import helper
import csv
import math

years, gdp, lgdp = [], [], []

with open('../swiss-gdp.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        years.append(int(row['Year']))
        gdp.append(float(row['GDPa']))
        lgdp.append(math.log(float(row['GDPa'])))

def predict(alpha, beta, xi):
    return beta * xi + alpha

alpha, beta = helper.sols(gdp, years)

print("alpha: %s, beta: %s" % (alpha, beta))


predicted = [predict(alpha, beta, xi) for xi in years]
errors = [y - p  for p, y in zip(predicted, gdp)]
sq_errors = [e * e for e in errors]
sse = sum(sq_errors)
tss = sum([ y * y for y in helper.de_mean(gdp)])
r_sq = 1.0 - sse / tss 
print("r-squared: %s " % r_sq)


plt.plot(years, gdp, '-bo', years, predicted, '-ro')
plt.title('Nominal Swiss GDP per year')
plt.ylabel('CHF')
plt.xlabel('Year')
plt.legend(['GDP', 'SOLS Trend'])
plt.show()
