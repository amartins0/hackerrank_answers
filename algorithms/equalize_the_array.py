#!/bin/python3

"""
Problem:
Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.
"""

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    biggest = Counter(arr).values()
    biggest = sorted(list(biggest), reverse=True)
    
    count = sum(biggest[1:])
    

    return count

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()