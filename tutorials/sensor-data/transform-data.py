#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexander Rüedlinger'
__license__ = 'MIT'

import argparse
import json


if __name__ == '__main__':
    description = 'Simple tool to transform sensor data to proper json data.'
    version = '0.1'
    MAX_BLKS_PER_DAY = int(24 * 60 * 60 / 14)

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-V', '--version', action='version', 
            version='%(prog)s {}'.format(version), 
            help='Print version number.')
    parser.add_argument('-o', '--output', dest='output', 
            help='JSON output file.', default='data.json')
    parser.add_argument('-i', '--input', dest='input', 
            help='Input file.')
  

    args = parser.parse_args()

    data = []

    with open(args.input, 'r') as f:
        for line in f.readlines():
            obs = json.loads(line)
            data.append(obs)

    with open(args.output, 'w+') as f:
        f.write(json.dumps(data, indent=4, separators=(',', ': ')))

