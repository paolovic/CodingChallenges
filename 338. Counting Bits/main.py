from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            dp[i] = 1 + dp[i - offset]
        return dp


s = Solution()
print(s.countBits(2))  # [0,1,1]

print(s.countBits(5))  # [0,1,1,2,1,2]
