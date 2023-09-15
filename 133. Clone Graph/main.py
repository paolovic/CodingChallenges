# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dummy = node
        p0 = dummy
        queue=[node]
        visited = set()

        while len(queue)>0:
            for _ in range(len(queue)):
                temp = queue.pop()
                visited.add(temp)
                p0 = Node(temp.val)
                for n in temp.neighbors:
                    p0.neighbors.append(Node(n.val))
                    if n not in visited:
                        queue.append(n)

