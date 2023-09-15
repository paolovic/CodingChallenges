#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#
import numpy as np

visited = set()
graph = {}


def componentsInGraph(gb):
    # Write your code here
    for edge in gb:
        if edge[0] in graph:
            graph[edge[0]].add(edge[1])
        else:
            graph[edge[0]] = {edge[1]}
        if edge[1] in graph:
            graph[edge[1]].add(edge[0])
        else:
            graph[edge[1]] = {edge[0]}

    smallest = np.inf
    largest = -np.inf
    for key in graph:
        count = countComponentsHelper(key)
        if count >= 2 and count < smallest:
            smallest = count
        if count >= 2 and count > largest:
            largest = count
    return [smallest, largest]


def countComponentsHelper(key: int) -> int:
    if key in visited:
        return 0
    visited.add(key)
    count = 1
    for val in graph[key]:
        count += countComponentsHelper(val)
    return count


bg = [[1, 17], [5, 13], [7, 12], [5, 17], [5, 12], [2, 17], [1, 18], [8, 13], [2, 15], [5, 20]]
print(componentsInGraph(bg)) # [11, 15]
