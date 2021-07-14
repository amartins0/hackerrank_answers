#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers():

    count = 0
    for i in range(int(input()), int(input())+1):
        i_square = str(i**2)
        right, left = i_square[len(i_square)//2:], i_square[0:len(i_square)//2]

        if right == '': right = 0
        if left == '': left = 0
        
        if int(right) + int(left) == i:
                print(i, end=' ')
                count += 1
                
    if count == 0: print( "INVALID RANGE")
            
    
if __name__ == '__main__':

    kaprekarNumbers()
