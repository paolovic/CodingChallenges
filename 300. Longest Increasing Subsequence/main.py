from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        max_length = 1
        for i in range(1, len(nums)):
            left = i-1
            while left>=0:
                if nums[i] > nums[left]:
                    dp[i]=max(dp[i], 1+dp[left])
                left-=1
            max_length=max(max_length, dp[i])

        return max_length

s = Solution()
nums = [0,1,0,3,2,3]
print(s.lengthOfLIS(nums))  # 4

nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))  # 4

nums = [7,7,7,7,7,7,7]
print(s.lengthOfLIS(nums))  # 1
