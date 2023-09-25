class Solution:
    def countSubstrings(self, s: str) -> int:
        self.counter = 0
        self.s = s
        for i in range(len(s)):
            left=i
            right=i
            self.isValidPalindrome(left, right)
            self.isValidPalindrome(left, right+1)
        return self.counter

    def isValidPalindrome(self, left, right):
        while left >=0 and right<len(self.s) and self.s[left]==self.s[right]:
            self.counter+=1
            left -= 1
            right += 1