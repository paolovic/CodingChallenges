from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(s)) for s in strs]
        mapping = {}
        for i in range(len(strs)):
            if mapping.get(sorted_strs[i]):
                mapping[sorted_strs[i]].append(strs[i])
            else:
                mapping[sorted_strs[i]] = [strs[i]]
        return list(mapping.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(s.groupAnagrams([""])) # [[""]]
print(s.groupAnagrams(["a"])) # [["a"]]