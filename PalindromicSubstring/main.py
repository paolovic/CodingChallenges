class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = len(s)
        for i in range(len(s)):
            left = i
            right = i
            while self.isValidPalindrome(s[left : right + 1]):
                counter += 1
                if right+1 < len(s):
                    right += 1
                if left-1 > -1:
                    left -= 1
        return counter

    def isValidPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


s = "abc"
sol = Solution()
print(sol.countSubstrings(s))  # 3

s = "aaa"
print(sol.countSubstrings(s))  # 6

s = "abba"
print(sol.countSubstrings(s))  # 6
