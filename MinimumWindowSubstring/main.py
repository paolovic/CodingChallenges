class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict={}
        for c in t:
            if c in t_dict:
                t_dict[c]+=1
            else:
                t_dict[c]=1
        windowSize = len(t)-1
        for i in range(len(s)-windowSize):
            for j in range(i, i+windowSize+1):
                if s[j] in t:
                    t[c]-=1
            
        pass


s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t))  # "BANC"

s = "a"
t = "a"
print(sol.minWindow(s, t))  # "a"

s = "a"
t = "aa"
print(sol.minWindow(s, t))  # ""
