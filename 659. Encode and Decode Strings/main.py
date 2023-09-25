from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        delimiter = "_$$_"
        return delimiter.join(strs)

    
    def decode(self, s: str) -> List[str]:
        delimiter = "_$$_"
        return s.split(delimiter)

# Test Case 1:
strs=["Hello","World", "how", "are", "you", "doing", "today?"]
s = Solution()
encoded = s.encode(strs)
print(encoded)
print(s.decode(encoded))

# Test Case 2:
strs=[""]
encoded = s.encode(strs)
print(encoded)
print(s.decode(encoded))
