class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res << 1
            if (n & 1)==1:
                res+=1
            n = n>>1
        return res


sol = Solution()
n = 0b00000010100101000001111010011100
print(sol.reverseBits(n))  # 964176192 (0b00111001011110000010100101000000)

n = 11111111111111111111111111111101
print(sol.reverseBits(n))  # 3221225471 (0b10111111111111111111111111111111)

n = 0b111111111111
print(sol.reverseBits(n))  # 4095 (0b00000000000000000000111111111111)
