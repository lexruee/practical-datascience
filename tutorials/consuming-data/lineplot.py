#!/usr/bin/env python

from matplotlib import pyplot as plt
import csv

years, gdp = [], []

with open('../swiss-gdp.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        years.append(row['Year'])
        gdp.append(row['GDPa'])        


plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title('Nominal Swiss GDP per year')
plt.ylabel('Billions of CHF')
plt.xlabel('Year')
plt.show()
