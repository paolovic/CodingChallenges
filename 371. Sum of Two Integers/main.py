class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a | b


s = Solution()
print(s.getSum(1, 2))  # 3
print(s.getSum(2, 3))  # 5
print(s.getSum(0, 0))  # 0
print(s.getSum(0, 1))  # 1
print(s.getSum(1, 0))  # 1
print(s.getSum(-1, 1))  # 0
