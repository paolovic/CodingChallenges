from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        odd = True if (m + n) % 2 != 0 else False
        left1 = 0
        right1 = m-1
        left2 = 0
        right2 = n-1
        
        pass


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
