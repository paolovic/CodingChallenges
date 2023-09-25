class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = [i for i in range(1, n + 1)]
        while len(queue) > 1:
            for _ in range(k-1):
                queue.append(queue.pop(0))
            queue.pop(0)
        return queue[0]


s = Solution()
print(s.findTheWinner(6, 6))  # 4
print(s.findTheWinner(5, 2))  # 3
print(s.findTheWinner(6, 5))  # 1
