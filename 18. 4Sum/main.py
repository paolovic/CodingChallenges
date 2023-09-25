from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        result = []
        curr = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k += 1
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1
        return result


s = Solution()
print(s.fourSum([2, 2, 2, 2, 2], 8))  # [[2,2,2,2]]
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum([], 0))  # []
print(s.fourSum([0], 0))  # []
print(s.fourSum([0, 0, 0, 0], 0))  # [[0,0,0,0]]
print(s.fourSum([-1, 0, 1, 2, -1, -4], -1))  # [[-4,0,1,2],[-1,-1,0,1]]
print(
    s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
)  # [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum([-5, 5, 4, -3, 0, 0, 4, -2], 4))  # [[-5,0,4,5],[-3,-2,4,5]]
print(s.fourSum([-1, 2, 2, -5, 0, -1, 4], 3))  # [[-5,2,2,4],[-1,0,2,2]]
print(
    s.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -9)
)  # [[-5,-4,-1,1],[-5,-4,0,0],[-5,-2,-2,0],[-4,-2,-2,-1]]
print(
    s.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -8)
)  # [[-5,-4,0,1],[-5,-2,-2,1],[-4,-2,-2,0]]
print(s.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -7))  # [[-5,-2,-2,0]]
print(s.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -6))  # [[-5,-1,0,0],[-4,-2,0,0]]
print(s.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -5))  # [[-5,0,0,0],[-4,-1,0,0]]
print(s.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -4))  # [[-4,0,0,0]]
