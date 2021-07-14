#!/bin/python3


"""
Problem:
Given a square matrix, calculate the absolute difference between the sums of its diagonals. 
"""


import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diagonals = []
    right_diagonals = []
    
    for i in range(len(arr)):
        left_diagonals.append(arr[i][i])
        right_diagonals.append(arr[i][len(arr)-i-1])
        
    return abs(sum(left_diagonals) - sum(right_diagonals))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()