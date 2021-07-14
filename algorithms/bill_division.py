#!/bin/python3

"""
Problem:
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.
"""

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
"""
    bill: an array of integers representing the cost of each item ordered
    k: an integer representing the zero-based index of the item Anna doesn't eat
    b: the amount of money that Anna contributed to the bill
"""

def bonAppetit(bill, k, b):
    split = int((sum(bill) - int(bill[k])) / 2)
    if split == b:
        print("Bon Appetit")
    else:
        print(b - split)
    

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)