from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append([i, j])

        for z in zeros:
            i, j = z

            matrix[i] = [0] * len(matrix[0])

            for row in matrix:
                row[j] = 0


s = Solution()

print(
    s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
)  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # [[1,0,1],[0,0,0],[1,0,1]]
