#!/bin/python3

"""
Problem:
Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces. Write a program that prints a staircase of size n. 
"""



import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for _ in range(1, n + 1):
        print(str(_ * '#').rjust(n))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
