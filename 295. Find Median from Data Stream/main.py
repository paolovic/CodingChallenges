class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        left = 0
        right = len(self.nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        self.nums.insert(left, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 != 0:
            return self.nums[n // 2]
        else:
            return (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
num = 1
obj.addNum(num)
num = 3
obj.addNum(num)
num = 1
obj.addNum(num)
param_2 = obj.findMedian()
