class Solution:
    def isPalindrome(self, x: int) -> bool:
        """if x == 0:
            return True
        if x < 0:
            return False
        temp = x
        compare = 0
        while x != 0:
            i = x % 10
            compare = compare * 10 + i
            x //= 10
        return compare == temp"""

        if x < 0:
            return False
        div = 1
        while x >= 10 * div:
            div *= 10
        while x != 0:
            right = x % 10
            left = x // div
            if left != right:
                return False
            x %= div
            x //= 10
            div //= 100
        return True


s = Solution()
print(s.isPalindrome(121))  # True
print(s.isPalindrome(-121))  # False
print(s.isPalindrome(10))  # False
print(s.isPalindrome(-101))  # False
print(s.isPalindrome(0))  # True
