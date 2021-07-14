#!/bin/python3

"""
Problem:
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.
"""

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = max = scores[0]
    min_count = max_count = 0
    
    for score in scores:
        print(score)
    
        if score < min:
            min = score
            min_count += 1
    
        if score > max:
            max = score
            max_count += 1
            
    return max_count, min_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()