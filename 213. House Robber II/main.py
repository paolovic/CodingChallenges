from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        if len(self.nums) == 1:
            return nums[0]
        if len(self.nums) == 2:
            return max(nums[0], nums[1])
        dp1 = [None for _ in range(len(nums))]
        dp2 = [None for _ in range(len(nums))]
        self.robTwice(0, len(self.nums) - 2, dp1)
        self.robTwice(1, len(self.nums) - 1, dp2)
        return max(dp1[len(nums) - 2], dp2[len(nums) - 1])

    def robTwice(self, i, numsLength, dp):
        dp[i] = self.nums[i]
        dp[i + 1] = max(self.nums[i], self.nums[i + 1])
        for j in range(i + 2, numsLength + 1):
            dp[j] = max(self.nums[j] + dp[j - 2], dp[j - 1])


s = Solution()
print(s.rob([1, 2, 3, 1]))  # 4

print(s.rob([2, 3, 2]))  # 3
