class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n!=0:
            sum+= n & 1
            n = n>>1
        return sum

s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))  # 3
print(s.hammingWeight(0b00000000000000000000000010000000))  # 1
print(s.hammingWeight(0b111                          ))  # 31
