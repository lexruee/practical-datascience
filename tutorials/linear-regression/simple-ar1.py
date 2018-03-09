#!/usr/bin/env python

from matplotlib import pyplot as plt
import helper
import csv

years, gdp = [], []

with open('../swiss-gdp.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        years.append(int(row['Year']))
        gdp.append(float(row['GDPa']))        

ys, xs = gdp[1:], gdp[:-1]

def predict(alpha, beta, xi):
    return beta * xi + alpha

alpha, beta = helper.sols(ys, xs)
print("alpha: %s, beta: %s" % (alpha, beta))

predicted = [predict(alpha, beta, xi) for xi in xs]
errors = [y - p  for p, y in zip(predicted, gdp)]
sq_errors = [e * e for e in errors]
sse = sum(sq_errors)
tss = sum([ y * y for y in helper.de_mean(gdp)])
r_sq = 1.0 - sse / tss 

print("r-squared: %s " % r_sq)

forecast_years = list(range(max(years), max(years)+6))
forecasts = [predicted[-1]]
for fyear in forecast_years[1:]:
    yi = forecasts[-1]

    fy = predict(alpha, beta, yi)
    forecasts.append(fy)

plt.plot(years, gdp, '-bo', years[1:], predicted, '-ro', forecast_years, forecasts, '-go')
plt.title('Nominal Swiss GDP per year')
plt.ylabel('CHF')
plt.xlabel('Year')
plt.legend(['GDP', 'AR(1)', 'Forecast'])
plt.xticks(range(min(years), max(forecast_years), 5))
plt.grid()
plt.show()
