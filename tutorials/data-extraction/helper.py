#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexander Rüedlinger'
__license__ = 'MIT'


from web3 import Web3, HTTPProvider

class Client:

    def __init__(self, url='http://localhost:8545'):
        self._url = url
        self._web3 = Web3(HTTPProvider(self._url))

    def get_blocks(self, num, block_step=1):
        num = int(num)
        current_block = self._web3.eth.blockNumber
        
        return [self._web3.eth.getBlock(ibn) for ibn in
                range(current_block-num-1, current_block+1, block_step)]

    def get_blocks_from(self, start_block, end_block=-1, block_step=1):
        start_block = int(start_block)
        end_block = self._web3.eth.blockNumber if end_block == -1 else end_block
        
        return [self._web3.eth.getBlock(ibn) for ibn in range(start_block,
            end_block+1, block_step)]

