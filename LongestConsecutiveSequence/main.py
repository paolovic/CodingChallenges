from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count=0
        for i in nums:
            if (i-1) not in nums:
                count = 1
                while i+1 in nums:
                    count+=1
                    i+=1
                max_count=max(count, max_count)
        return max_count
    



s = Solution()
print(s.longestConsecutive([1, 2, 0, 1]))  # 3
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 9]))  # 10
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 9, 10]))  # 11
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 9, 10, 11]))  # 12
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 9, 10, 11, 12]))  # 13
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 9, 10, 11, 12, 13]))  # 14
