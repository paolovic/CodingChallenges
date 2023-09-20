from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adjacency = {}
        for p in prerequisites:
            if p[0] not in self.adjacency:
                self.adjacency[p[0]] = [p[1]]
            else:
                self.adjacency[p[0]].append(p[1])
        self.visited = set()
        for key in self.adjacency:
            if not self.dfs(key):
                return False
        return True

    def dfs(self, course) -> bool:
        if course in self.visited:
            return False
        if course in self.adjacency and self.adjacency[course] == []:
            return True
        self.visited.add(course)
        if course in self.adjacency:
            for prerequisite in self.adjacency[course]:
                if not self.dfs(prerequisite):
                    return False
        self.visited.remove(course)
        if course in self.adjacency:
            self.adjacency[course] = []
        return True


s = Solution()
numCourses = 3
prerequisites = [[1, 0], [0, 2], [2, 1]]
print(s.canFinish(numCourses, prerequisites))  # False


numCourses = 2
prerequisites = [[1, 0]]
print(s.canFinish(numCourses, prerequisites))  # True

numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(s.canFinish(numCourses, prerequisites))  # False


numCourses = 3
prerequisites = [[1, 0], [2, 0], [1, 2]]
print(s.canFinish(numCourses, prerequisites))  # True
