import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = re.sub(r'[^a-z0-9]','', s.lower())
        left = 0
        right = len(s) - 1
        while left<right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True

s = Solution()
# Test Case 1:
print(s.isPalindrome("abba"))  # Expected: True

# Test Case 2:
print(s.isPalindrome("abcba"))  # Expected: True

# Test Case 3:
print(s.isPalindrome("abca"))  # Expected: False

# Test Case 4:
print(s.isPalindrome("A man, a plan, a canal: Panama")) 
