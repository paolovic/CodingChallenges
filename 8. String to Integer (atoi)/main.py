class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        isNeg = False
        res = 0
        for i in range(index, len(s)):
            if s[i] == " ":
                index += 1
            else:
                break

        if index < len(s) and (s[index] == "-" or s[index] == "+"):
            isNeg = s[index] == "-"
            index += 1

        for i in range(index, len(s)):
            num = ord(s[i]) - 48
            if num < 0 or num > 9:
                break
            else:
                res *= 10
                res += num

        if isNeg:
            res *= -1
            res = max(pow(-2, 31), res)
        else:
            res = min(pow(2, 31) - 1, res)
        return res


sol = Solution()
s = "-+123"
print(sol.myAtoi(s))  # 1


s = "words and 987"
print(sol.myAtoi(s))  # 0


s = "   -42"
print(sol.myAtoi(s))  # -42


s = "42"
print(sol.myAtoi(s))  # 42


s = "4193 with words"
print(sol.myAtoi(s))  # 4193
