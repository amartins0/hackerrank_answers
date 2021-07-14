"""
Problem:
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with places after the decimal.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    zero=0

    for n in arr:
        if n >0:
            pos +=1
        elif n<0:
            neg +=1
        elif n ==0:
            zero +=1
    print(    "{:.6f}".format(pos/len(arr)) +"\n" +"{:.6f}".format(neg/len(arr))+ "\n" +"{:.6f}".format(zero/len(arr)))
    return "{:.6f}".format(pos/len(arr)) +"\n" +"{:.6f}".format(neg/len(arr))+ "\n" +"{:.6f}".format(zero/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
