#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

import copy
import numpy as np

def cutTheTree(data, edges):
    graph={}
    for e in edges:
        if e[0] in graph:
            graph[e[0]].add(e[1])
        else:
            graph[e[0]]={e[1]}
        if e[1] in graph:
            graph[e[1]].add(e[0])
        else:
            graph[e[1]]={e[0]}
    total = traverse(graph, data, None)
    min_ = np.inf
    for e in edges:
        sum = traverse(graph, data, e[1])
        compliment = abs(total-sum)
        min_ = min(min_, abs(compliment-sum))

    # Write your code here

def traverse(graph, data, toCut):
    sum=0
    stack = [1]
    visited={1}
    while len(stack)>0:
        node = stack.pop()
        sum+=data[node-1]
        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor != toCut:
                    visited.add(neighbor)
                    stack.append(neighbor)
    return sum

data = [100, 200, 100, 500, 100, 600]
edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
print(cutTheTree(data, edges)) # 400

