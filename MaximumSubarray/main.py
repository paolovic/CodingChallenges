from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i], nums[i] + curr_max)
            max_sum = max(max_sum, curr_max)
        return max_sum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(s.maxSubArray([1]))  # 1
print(s.maxSubArray([5, 4, -1, 7, 8]))  # 23
