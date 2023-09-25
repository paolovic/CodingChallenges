class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*n for _ in range(m)]
        arr[0] = [1]*n
        for i in range(m):
            arr[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i-1][j]+arr[i][j-1]
        return arr[m-1][n-1]


s = Solution()
print(s.uniquePaths(3, 3)) # 6
print(s.uniquePaths(3, 7)) # 28
print(s.uniquePaths(3, 2)) # 3
print(s.uniquePaths(7, 3)) # 28
print(s.uniquePaths(1, 1)) # 1


    