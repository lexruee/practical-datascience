#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexander Rüedlinger'
__license__ = 'MIT'

from helper import Client 
from datetime import datetime
import math
import argparse
import sys
import json


if __name__ == '__main__':
    description = 'ethdx - Simple tool to extract data from eth blockchains'
    version = '0.1'
    MAX_BLKS_PER_DAY = int(24 * 60 * 60 / 14)

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-V', '--version', action='version', 
            version='%(prog)s {}'.format(version), 
            help='Print version number.')
    parser.add_argument('-a', '--jsonrpc', dest='jsonrpc', 
            help='Set JSONRPC URL address.', default='http://localhost:8485')
    parser.add_argument('-s', '--start-block', dest='start_block', type=int,
            help='Set start block.', default=1)
    parser.add_argument('-e', '--end-block', dest='end_block', type=int,
            help='Set end block.', default=MAX_BLKS_PER_DAY * 30 * 4)
    parser.add_argument('-r', '--sampling-rate', dest='sampling_rate', type=float,
            help='Set sampling rate (value r e [0,1]).', default=0.1)
    parser.add_argument('-o', '--output', dest='output', 
            help='JSON output file.', default='data.json')
  
    args = parser.parse_args()

    
    block_step = int(args.sampling_rate * MAX_BLKS_PER_DAY)
    start_block, end_block = args.start_block, args.end_block
    data = []

    try:
        client = Client(args.jsonrpc)
        blocks = client.get_blocks_from(start_block, end_block, block_step)
    except:
        print("Failed to fetch data from %s" % args.jsonrpc)
        sys.exit(1)

    def fix(s):
        if type(s) in [int, float, str, list, dict]:
            return s
        else:
            return str(s)

    for block in blocks:
        d = {k:block[k] for k in block}
        data.append(d)

    with open(args.output, 'w+') as f:
        f.write(json.dumps(data, indent=4, separators=(',', ': ')))

    #diffs = [block['difficulty']/1000**4 for block in blocks]
    #timestamps = [block['timestamp'] for block in blocks]
    #dates = [datetime.fromtimestamp(int(t)) for t in timestamps]

