from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def reflect(self, matrix):
        for row in matrix:
            for i in range(len(row)//2):
                temp = row[i]
                row[i] = row[len(row)-1-i]
                row[len(row)-1-i] = temp


    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                if i!=j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp


s = Solution()

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s.rotate(matrix)
print(matrix)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(matrix)
print(matrix)  # [[7,4,1],[8,5,2],[9,6,3]]


matrix = [[1]]
s.rotate(matrix)
print(matrix)  # [[1]]

matrix = [[1, 2], [3, 4]]
s.rotate(matrix)
print(matrix)  # [[3,1],[4,2]]
