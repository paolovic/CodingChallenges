from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for i in range(len(nums)):
            xor = xor ^ i ^ nums[i]
        return xor


s = Solution()
nums = [3,0,1]
print(s.missingNumber(nums)) # 2

nums = [0,1]
print(s.missingNumber(nums)) # 2

nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums)) # 8

