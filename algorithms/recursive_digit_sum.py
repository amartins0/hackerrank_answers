#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(n,k):
    n = str(sum([int(i) for i in n])*k); k=1
   
    if len(str(n)) == 1:
        return n
    
    else:
        return superDigit(str(n), k)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
