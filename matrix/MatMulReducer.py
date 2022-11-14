#!/usr/bin/python

"""
Reducer for matrix multiplication with Hadoop MapReduce.

Acknowledge:    This code is modified from Risheng WANG's code 
                in Week 8 Lecture slide.
Note:   This is just for your reference. 
        Feel free to change it for your preference.
"""

import sys

import binascii
import struct
import fileinput
import pdb

BLOCKSZIE = 128
TOTALSIZE = 1024
NB = TOTALSIZE/BLOCKSZIE

LeftMatrixBlock = []
RightTransposeMatrixBlock = []

# total number of lines (within)
nl = 0

# old block no = -1
blockno = -1

#for line in sys.stdin:
for line in fileinput.input():
    # for debug
    # nl = nl + 1
    
    nl = nl + 1
    # remove leading and trailing whitespace
    line = line.strip()
    # parse input
    input_key, input_value = line.split("\t", 1)

    # for debug
    # print input_key

    blockno = int(input_key)
    A_B, index, row_value = input_value.split(":")

    if A_B == "L":
        LeftMatrixBlock.append(row_value.split(" "))
    if A_B == "R":
        RightTransposeMatrixBlock.append(row_value.split(" "))

    # an block is finished
    if (nl == 2 * BLOCKSZIE):
        # result nl
        nl = 0
        # print blcok number to  mark the output
        print(blockno, BLOCKSZIE)

res = [[0 for col in range(BLOCKSZIE)] for row in range(BLOCKSZIE)]
for i in range(BLOCKSZIE):
    for j in range(BLOCKSZIE):
        for k in range(TOTALSIZE):
            #print(LeftMatrixBlock[i][k][2:])
            #print(LeftMatrixBlock[i][k][2:])
            #print(binascii.a2b_hex(LeftMatrixBlock[i][k][2:]))
            #pdb.set_trace()
            left_val = int(struct.unpack("I", binascii.a2b_hex(LeftMatrixBlock[i][k][2:]))[0])
            right_val = int(struct.unpack("I", binascii.a2b_hex(RightTransposeMatrixBlock[j][k][2:]))[0])

            #print(left_val, right_val)
            #pdb.set_trace()
            #left_val = struct.unpack("!f", binascii.a2b_hex(LeftMatrixBlock[i][k]))[0]
            #right_val = struct.unpack("!f", binascii.a2b_hex(RightTransposeMatrixBlock[j][k]))[0]
            res[i][j] += left_val * right_val
        print(res[i][j])
    #print
del LeftMatrixBlock[:]
del RightTransposeMatrixBlock[:]
