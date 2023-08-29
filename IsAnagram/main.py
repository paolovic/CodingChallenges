class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency = {}
        for c in s:
            if c in frequency:
                frequency[c] += 1
            else:
                frequency[c] = 1

        for c in t:
            if c not in frequency or frequency[c] == 0:
                return False
            else:
                frequency[c] -= 1

        return True


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))  # True

s = "rat"
t = "car"
print(Solution().isAnagram(s, t))  # False

s = "a"
t = "ab"
print(Solution().isAnagram(s, t))  # False

s = "aacc"
t = "ccac"
print(Solution().isAnagram(s, t))  # False
