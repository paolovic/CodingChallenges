from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0


s = Solution()
nums = [2, 3, 1, 1, 4]
print(s.canJump(nums))  # True

nums = [3, 2, 1, 0, 4]
print(s.canJump(nums))  # False

nums = [0]
print(s.canJump(nums))  # True

nums = [1, 0, 1, 0]
print(s.canJump(nums))  # False

nums = [1, 1, 1, 0]
print(s.canJump(nums))  # True
