class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.left = 0
        self.right = 0
        for i in range(len(s)):
            self.longestPalindromeHelper(i, i)
            self.longestPalindromeHelper(i, i + 1)
        return self.s[self.left : self.right + 1]

    def longestPalindromeHelper(self, left, right):
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            left -= 1
            right += 1
        if (right - 1) - (left + 1) > self.right - self.left:
            self.left = left + 1
            self.right = right - 1


s = Solution()
print(s.longestPalindrome("babad"))  # "bab"
print(s.longestPalindrome("cbbd"))  # "bb"
print(s.longestPalindrome("a"))  # "a"
print(s.longestPalindrome("ac"))  # "a"
print(s.longestPalindrome("bb"))  # "bb"
print(s.longestPalindrome("ccc"))  # "ccc"
print(s.longestPalindrome("aaaa"))  # "aaaa"
