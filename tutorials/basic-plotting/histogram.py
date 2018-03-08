#!/usr/bin/env python

from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar(histogram.keys(), histogram.values(), 8)
plt.title('Distribution of Exam 1 Grades')
plt.ylabel('# of Students')
plt.xlabel('Grades')
plt.show()
