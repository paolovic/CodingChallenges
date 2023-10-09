class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        """res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res"""

        direction = False
        count = 0

        arr = ["" for i in range(numRows)]

        for i in range(len(s)):
            curr = s[i]

            arr[count] += curr
            if count == 0 or count >= numRows - 1:
                direction = not direction
            if direction:
                count += 1
            else:
                count -= 1

        return "".join(arr)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
print(s.convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
print(s.convert("A", 1))  # A
