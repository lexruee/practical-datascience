#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import matplotlib.pyplot as plt
from matplotlib import dates
import numpy as np
from datetime import datetime
import argparse


def create_plot(data):
    temperature = []
    humidity= []
    pressure = []
    timestamp = []
    for row in data:
        temperature.append(row['temperature'])
        humidity.append(row['humidity'])
        pressure.append(row['pressure'])
        timestamp.append(row['timestamp'])

    time = [datetime.fromtimestamp(t) for t in timestamp]
    min_time, max_time = min(time), max(time)

    hfmt = dates.DateFormatter('%m/%d %H:%M')
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
    fig.suptitle('BME280 Sensor data from %s during %s to %s' %
            (min_time.strftime('%d. %b. %Y'), min_time.strftime('%H:%M:%S'), 
                max_time.strftime('%H:%M:%S')))

    ax1.xaxis.set_major_locator(dates.HourLocator(interval=1))
    ax1.xaxis.set_minor_locator(dates.MinuteLocator(interval=15))
    ax1.xaxis.set_major_formatter(hfmt)
    ax1.set_xticks(np.arange(0,24,1))
    ax1.plot(time, temperature)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Temperature in C')
    #ax1.set_xlim(min(time),max(time))


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
    
    return plt


if __name__ == '__main__':
    description = 'Simple tool to plot bme280 sensor data'
    version = '0.1'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-V', '--version', action='version', 
            version='%(prog)s {}'.format(version), 
            help='Print version number.')
    parser.add_argument('-o', '--output', dest='output', 
            help='Plot output file.', default='plot.png')
    parser.add_argument('-i', '--input', dest='input', 
            help='JSON input file.')
    parser.add_argument('-S', '--show', dest='show', 
                help='Show plot.', action='store_true')
  
    args = parser.parse_args()
 
    with open('sensor-data-17-3-2018.json', 'r') as f:
        data = json.loads(f.read())

    plt = create_plot(data)
     
    if args.output:
        plt.savefig(args.output)
    
    if args.show:
        plt.show()

