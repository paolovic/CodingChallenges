from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    counter += self.numIslandsHelper(grid, i, j)
        return counter

    def numIslandsHelper(self, grid, i, j):
        if (
            i < 0
            or i > len(grid) - 1
            or j < 0
            or j > len(grid[0]) - 1
            or grid[i][j] == "0"
        ):
            return
        grid[i][j] = "0"
        self.numIslandsHelper(grid, i - 1, j)
        self.numIslandsHelper(grid, i + 1, j)
        self.numIslandsHelper(grid, i, j - 1)
        self.numIslandsHelper(grid, i, j + 1)
        return 1


s = Solution()

print(
    s.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)  # 1
print(
    s.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)  # 3
print(s.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))  # 1
print(
    s.numIslands(
        [
            ["1", "0", "1", "1", "1"],
            ["1", "0", "1", "0", "1"],
            ["1", "1", "1", "0", "1"],
        ]
    )
)  # 1
print(
    s.numIslands(
        [
            ["1", "1", "1", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0", "0", "1"],
            ["1", "1", "1", "1", "1", "0", "1"],
            ["1", "0", "0", "0", "1", "0", "1"],
            ["1", "0", "1", "0", "1", "0", "1"],
            ["1", "0", "1", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "1", "1", "1"],
        ]
    )
)  # 1
