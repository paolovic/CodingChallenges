class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        chars = set()
        longest = 0
        right = 0
        while right < len(s):
            letter = s[right]
            if letter not in chars:
                chars.add(letter)
                longest = max(longest, len(chars))
                right+=1
            else:
                chars.remove(s[left])
                left += 1
        return longest


s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))  # 3

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))  # 1

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))  # 3

s = ""
print(Solution().lengthOfLongestSubstring(s))  # 0
