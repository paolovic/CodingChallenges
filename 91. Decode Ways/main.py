class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s)+1):
            if int(s[i-1])>=1 and int(s[i-1])<=9:
                dp[i]+=dp[i-1]
            if int(s[i-2:i])>=10 and int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
        return dp[len(s)]

sol = Solution()
s = "226"
print(sol.numDecodings(s))  # 3

s = "12"
print(sol.numDecodings(s))  # 2

s = "06"
print(sol.numDecodings(s))  # 0