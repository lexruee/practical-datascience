#!/usr/bin/env python

from matplotlib import pyplot as plt
import csv
import math

years, gdp = [], []

with open('../swiss-gdp.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        years.append(int(row['Year']))
        gdp.append(float(row['GDPa']))

plt.plot(years, gdp, '-bo')
plt.title('Nominal Swiss GDP per year')
plt.ylabel('CHF')
plt.xlabel('Year')
plt.xticks(range(min(years), max(years)+1, 5))
plt.show()
