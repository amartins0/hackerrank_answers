#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#
#p = price, d = value to subtract, m = lower bound, s = budget

def howManyGames(p, d, m, s):
    price = budget = p
    count = 0

    while budget <= s:
        if price - d >= m:
            price -=d
            budget += price
            count += 1
        
        else:
            price = m
            budget += price
            count += 1
    
            
    return count
    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
