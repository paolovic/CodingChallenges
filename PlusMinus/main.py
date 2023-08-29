#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
    print("{:.6f}".format(pos/n))
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zero/n))
    # Write your code here


if __name__ == "__main__":
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    n = 6
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)

    n = 8
    arr = [1, 2, 3, -1, -2, -3, 0, 0]

    plusMinus(arr)
