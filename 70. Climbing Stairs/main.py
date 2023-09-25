class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        prev = 1
        prev2 = 1
        for i in range(2, n+1):
            curr = prev + prev2
            prev = prev2
            prev2 = curr
        return prev2


s = Solution()
print(s.climbStairs(2))  # 2
print(s.climbStairs(3))  # 3
print(s.climbStairs(4))  # 5
print(s.climbStairs(5))  # 8
print(s.climbStairs(6))  # 13
print(s.climbStairs(7))  # 21