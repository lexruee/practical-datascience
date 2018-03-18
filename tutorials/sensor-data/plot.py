#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import matplotlib.pyplot as plt
from matplotlib import dates
import numpy as np
from datetime import datetime

data = []
temperature = []
humidity= []
pressure = []
timestamp = []
time = []

with open('sensor-data.json', 'r') as f:
    data = json.loads(f.read())
    for row in data:
        temperature.append(row['temperature'])
        humidity.append(row['humidity'])
        pressure.append(row['pressure'])
        timestamp.append(row['timestamp'])

time = [datetime.fromtimestamp(t) for t in timestamp]

hfmt = dates.DateFormatter('%m/%d %H:%M')
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
fig.suptitle('Sensor data from BME280')

ax1.xaxis.set_major_locator(dates.HourLocator(interval=1))
ax1.xaxis.set_minor_locator(dates.MinuteLocator(interval=15))
ax1.xaxis.set_major_formatter(hfmt)
ax1.plot(time, temperature)
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature in C')
ax1.set_xlim(min(time),max(time))


ax2.plot(time, humidity)
ax2.set_xlabel('Time')
ax2.set_ylabel('Humidity in percentage')

ax3.plot(time, pressure)
ax3.set_xlabel('Time')
ax3.set_ylabel('Pressure in Pa')


for ax in fig.axes:
    plt.sca(ax)
    ax.grid()

plt.xticks(rotation=45)
plt.show()
