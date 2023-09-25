from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        size = len(matrix) * len(matrix[0])
        nums = []
        while len(nums) < size:
            if len(nums) < size:
                for i in range(left, right + 1):
                    nums.append(matrix[top][i])
                top += 1
            if len(nums) < size:
                for i in range(top, bottom + 1):
                    nums.append(matrix[i][right])
                right -= 1
            if len(nums) < size:
                for i in range(right, left - 1, -1):
                    nums.append(matrix[bottom][i])
                bottom -= 1
            if len(nums) < size:
                for i in range(bottom, top - 1, -1):
                    nums.append(matrix[i][left])
                left += 1
        return nums


s = Solution()

print(s.spiralOrder([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))  # [1,2,3,4,5,6,7,8,9,10]
print(
    s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
)
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
print(s.spiralOrder([[1]]))  # [1]
print(
    s.spiralOrder([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
)  # [1,2,3,4,5,6,7,8,9,10]
