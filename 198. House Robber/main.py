from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = nums[:1] +[max(nums[:2])] + [0] * (len(nums) - 2)
        max_elm = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] =  max(nums[i]+dp[i-2], dp[i-1])
            max_elm = max(dp[i], max_elm)
        return max_elm


s = Solution()
print(s.rob([2, 1, 1, 2]))  # 4
print(s.rob([1, 2, 3, 1]))  # 4
print(s.rob([2, 7, 9, 3, 1]))  # 12

