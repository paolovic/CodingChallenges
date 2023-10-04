from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            B, A = A, B

        left = 0
        right = len(A) - 1

        while True:
            midA = (left + right) // 2
            midB = half - midA - 2

            ALeft = A[midA] if midA >= 0 else float("-infinity")
            ARight = A[midA + 1] if midA + 1 < len(A) else float("infinity")
            BLeft = B[midB] if midB >= 0 else float("-infinity")
            BRight = B[midB + 1] if midB + 1 < len(B) else float("infinity")

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 1:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                right = midA - 1
            else:
                left = midA + 1


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
