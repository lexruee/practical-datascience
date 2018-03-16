#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexander Rüedlinger'
__license__ = 'MIT'

import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import numpy as np
from dateutil.relativedelta import relativedelta
import math
import argparse
import sys
import json


def create_diff_plot(dates, diffs):
    plt.plot(dates, diffs)
    plt.title('Ella Difficulty')
    plt.xlabel('Time')
    plt.ylabel('Difficulty in T')
    plt.yticks(np.arange(0, max(diffs) + 1, 0.5))

    datemin = min(dates) - relativedelta(days=+1)
    datemax = max(dates) + relativedelta(days=+1)

    plt.xlim(datemin, datemax)
    plt.gca().xaxis.set_minor_locator(mdates.DayLocator())
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    monthsFmt = DateFormatter("%b '%y")
    plt.gca().xaxis.set_major_formatter(monthsFmt)

    plt.gcf().autofmt_xdate()
    plt.grid()
    return plt 


if __name__ == '__main__':
    description = 'ellap - Simple tool to plot ella difficulty'
    version = '0.1'
    MAX_BLKS_PER_DAY = int(24 * 60 * 60 / 14)

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-V', '--version', action='version', 
            version='%(prog)s {}'.format(version), 
            help='Print version number.')
    parser.add_argument('-o', '--output', dest='output', 
            help='Plot output file.', default='ella-diff.png')
    parser.add_argument('-i', '--input', dest='input', 
            help='JSON input file.')
    parser.add_argument('-S', '--show', dest='show', 
                help='Show plot.', action='store_true')
  
    args = parser.parse_args()
    
    try:
        with open(args.input, 'r') as f:
            blocks = json.loads(f.read())
    except:
        print("Failed to read data from %s" % arinputt)
        sys.exit(1)

    diffs = [block['difficulty']/1000**4 for block in blocks]
    timestamps = [block['timestamp'] for block in blocks]
    dates = [datetime.fromtimestamp(int(t)) for t in timestamps]

    plt = create_diff_plot(dates, diffs)
 
    if args.output:
        plt.savefig(args.output)
    
    if args.show:
        plt.show()

