#!/usr/bin/env python
# coding=utf-8
# http://python.jobbole.com/88907/
#  用不到 50 行的 Python 代码构建最小的区块链


import hashlib as hasher
import datetime as date


def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()


if __name__ == '__main__':
    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # How many blocks should we add to the chain
    # after the genesis block
    num_of_blocks_to_add = 20

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print "Block #{} has been added to the blockchain!".format(block_to_add.index)
        print "Hash: {}\n".format(block_to_add.hash)
