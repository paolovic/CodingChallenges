from typing import List

class Solution:
    def countComponents(self, edges: List[List[int]]) -> int:
        """if len(edges)==0:
            return 0
        start = 0
        end = 1
        count = 0
        paths={}

        for curr in edges:
            if curr[start] not in paths:
                count+=1
            paths[curr[end]]=curr[start]

        return count"""
        count = 0
        self.visited = set()
        self.adjacencyList = {}
        for e in edges:
            if e[0] in self.adjacencyList:
                self.adjacencyList[e[0]].append(e[1])
            else:
                self.adjacencyList[e[0]] = [e[1]]
            if e[1] in self.adjacencyList:
                self.adjacencyList[e[1]].append(e[0])
            else:
                self.adjacencyList[e[1]] = [e[0]]
        for key in self.adjacencyList:
            count += self.countComponentsHelper(key)
        return count

    def countComponentsHelper(self, key:int) -> int:
        if key in self.visited:
            return 0
    
        self.visited.add(key)
        for val in self.adjacencyList[key]:
            self.countComponentsHelper(val)
        return 1



s = Solution()
edges = [[0, 1], [1, 2], [3, 4]]
print(s.countComponents(edges))  # 2

edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(s.countComponents(edges))  # 1

edges1 = [[0, 1], [1, 2], [2, 0], [3, 4]]
print(s.countComponents(edges1))  # 2

edges2 = [[0, 1], [2, 3], [4, 5], [6, 7]]
print(s.countComponents(edges2))  # 4

edges3 = [[0, 1], [1, 2], [3, 4], [4, 5]]
print(s.countComponents(edges3))  # 2

edges4 = []
print(s.countComponents(edges4))  # 0

edges5 = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]
print(s.countComponents(edges5))  # 2

edges6 = [[0, 1], [1, 2], [3, 4], [4, 5], [6, 7], [7, 8]]
print(s.countComponents(edges6))  # 3

