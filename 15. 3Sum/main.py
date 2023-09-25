from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1

        return result


s = Solution()
print(s.threeSum([1,-1,-1,0]))  # []
print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(s.threeSum([]))  # []
print(s.threeSum([0]))  # []
