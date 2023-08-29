from typing import List

import numpy as np


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [np.inf] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(1 + dp[i - c], dp[i])
        return dp[amount] if dp[amount] != np.inf else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))  # 3
print(s.coinChange([2], 3))  # -1
print(s.coinChange([1], 0))  # 0
print(s.coinChange([1], 1))  # 1
print(s.coinChange([1], 2))  # 2
print(s.coinChange([1, 2, 5], 100))  # 20
print(s.coinChange([186, 419, 83, 408], 6249))  # 20
print(s.coinChange([1, 2, 5], 11))  # 3
