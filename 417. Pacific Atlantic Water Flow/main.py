from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.m = len(self.heights)
        self.n = len(self.heights[0])

        pac_queue = []
        atl_queue = []
        for j in range(self.n):
            pac_queue.append([0, j])
            atl_queue.append([self.m - 1, j])
        for i in range(self.m):
            pac_queue.append([i, 0])
            atl_queue.append([i, self.n - 1])

        atlantic = self.bfs(atl_queue)
        pacific = self.bfs(pac_queue)

        result = []
        for i in range(self.m):
            for j in range(self.n):
                if atlantic[i][j] and pacific[i][j]:
                    result.append([i, j])

        return result

    def bfs(self, queue):
        visited = [[False] * self.n for _ in range(self.m)]

        isValid = lambda x, y: x >= 0 and x < self.m and y >= 0 and y < self.n

        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        while len(queue) > 0:
            x, y = queue.pop(0)
            visited[x][y] = True
            for d in directions:
                i, j = x + d[0], y + d[1]
                if not isValid(i, j) or visited[i][j]:
                    continue
                if self.heights[i][j] >= self.heights[x][y]:
                    queue.append([i, j])

        return visited


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]

solution = Solution()
print(solution.pacificAtlantic(heights))  # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

heights = [
    [2, 1],
    [1, 2],
]

print(solution.pacificAtlantic(heights))  # [[0,0],[0,1],[1,0],[1,1]]

heights = [[1]]
print(solution.pacificAtlantic(heights))  # [[0,0]]
