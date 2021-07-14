#!/bin/python3

"""
Problem:
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
"""

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    
    for sock in set(ar):
        pairs += ar.count(sock)//2
    
    
    return pairs
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()