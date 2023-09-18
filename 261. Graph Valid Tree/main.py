from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adjacency = {}
        for e in edges:
            if e[0] not in self.adjacency:
                self.adjacency[e[0]] = [e[1]]
            else:
                self.adjacency[e[0]].append(e[1])
            if e[1] not in self.adjacency:
                self.adjacency[e[1]] = [e[0]]
            else:
                self.adjacency[e[1]].append(e[0])
        self.visited = set()
        return not self.checkCycle(0, -1)

    def checkCycle(self, node, parent):
        self.visited.add(node)
        for neighbor in self.adjacency[node]:
            if neighbor in self.visited:
                if neighbor != parent:
                    return True
            else:
                if self.checkCycle(neighbor, node):
                    return True
        return False


s = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(s.validTree(n, edges))  # True

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(s.validTree(n, edges))  # False
