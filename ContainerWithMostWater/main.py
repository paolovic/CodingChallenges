from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            maxArea = max((right-left)*min(height[left], height[right]), maxArea)
            if(height[left]>height[right]):
                right-=1
            else:
                left+=1
        return maxArea


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(s.maxArea([1, 1]))  # 1
print(s.maxArea([4, 3, 2, 1, 4]))  # 16
print(s.maxArea([1, 2, 1]))  # 2
