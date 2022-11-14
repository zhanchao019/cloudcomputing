#!/usr/bin/python

"""
Mapper for matrix multiplication with Hadoop MapReduce.

Acknowledge:    This code is modified from Risheng WANG's code 
                in Week 8 Lecture slide.
Note:   This is just for your reference. 
        Feel free to change it for your preference.
"""

import sys
import os
import fileinput

# BLOCKSIZE must be the intergral power of two
BLOCKSIZE = 128
TOTALSIZE = 1024

# number of blocks for Matrix A/B
NB = int(TOTALSIZE/BLOCKSIZE)

# matrix_file = os.path.join(".", 'DataInHW8.14', 'combine.txt')
# matrix_file = open(matrix_file, 'r')
# matrix = matrix_file.read()

#line = sys.stdin.readline()
# matrix = matrix.split('\n')

# input comes from STDIN (standard input)
#line = sys.stdin.readline()
# for line in sys.stdin.readlines():
#while line != '':
for line in fileinput.input():

    # remvoe leading and trailing whitespace
    line = line.strip()
    # parse the input
    A_B, lineno, row_value = line.split(" ", 2)
    
    if A_B == "L":
        ib = (int)(lineno)/BLOCKSIZE  # note here the input data starts from 1, the result may differ from that in ppt
        for jb in range(NB):
            # the key is the BLOCK Number
            intermediate_key = '%05d'%(ib * NB + jb)
            # the value is the {L/R}:{LineNo}:{values of current line}
            intermediate_value = 'L:%s:%s'%(lineno, row_value)
            # key and value are seperated by a tab
            print("%s\t%s" % (intermediate_key, intermediate_value))

    if A_B == "R":
        jb = (int)(lineno)/BLOCKSIZE
        for ib in range(NB):
            intermediate_key = '%05d'%(ib * NB + jb)
            intermediate_value = 'R:%s:%s'%(lineno, row_value)
            print("%s\t%s"%(intermediate_key, intermediate_value))
    
    #line = sys.stdin.readline()


# matrix_file.close()
