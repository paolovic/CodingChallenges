from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [[] for _ in range(target+1)]
        for i in range(1, len(dp)):
            for c in candidates:
                if i==c:
                    dp[i].append(c)
                elif c<i and dp[i-c]:
                    dp[i]=1
        pass


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]
print(s.combinationSum([2, 3, 5], 8))  # [[2,2,2,2],[2,3,3],[3,5]]
print(s.combinationSum([2], 1))  # []
