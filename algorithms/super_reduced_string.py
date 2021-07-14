#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    
    for i in s:
        if i+i in s:
            s = s.replace(str(i+i), "")

    return "Empty String" if not s else s

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()