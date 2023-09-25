class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if s[0] == ")" or s[0] == "]" or s[0] == "}" or len(s) == 1:
            return False
        stack = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if (
                    (i == ")" and prev != "(")
                    or (i == "]" and prev != "[")
                    or (i == "}" and prev != "{")
                ):
                    return False
        return len(stack) == 0


s = Solution()
# Test Case 1:
s0 = "(){}}{" # Expected: False
print(s.isValid(s0))

s1 = "()" # Expected: True
print(s.isValid(s1))

# Test Case 2:
s2 = "()[]{}" # Expected: True
print(s.isValid(s2))

# Test Case 3:
s3 = "(]" # Expected: False
print(s.isValid(s3))

# Test Case 4:
s4 = "([)]" # Expected: False
print(s.isValid(s4))
