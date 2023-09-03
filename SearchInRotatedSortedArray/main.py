from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >=nums[left]:
                    right = mid - 1
                else:
                    left = mid+1

        return -1


s = Solution()
print(s.search([5, 1, 3], 5))  # 4
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
print(s.search([1], 0))  # -1
print(s.search([1, 3], 3))  # 1
