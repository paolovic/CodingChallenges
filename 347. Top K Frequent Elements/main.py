from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        bucket = []
        res = []
        for i in nums:
            if i in frequency:
                frequency[i] +=1
            else:
                frequency[i] =1
        
        for num, freq in frequency.items():
            while len(bucket) <= freq:
                bucket.append(None)
            if bucket[freq] is not None:
                bucket[freq].add(num)
            else:
                bucket[freq] = {num}
        
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i] is not None:
                for elm in bucket[i]:
                    res.append(elm)
            if len(res)==k:
                return res



s = Solution()
nums = [1, 2]
k = 2
print(s.topKFrequent(nums, k))  # [1,2]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(s.topKFrequent(nums, k))  # [1,2]

nums = [1]
k = 1
print(s.topKFrequent(nums, k))  # [1]

nums = [1, 2, 2]
k = 1
print(s.topKFrequent(nums, k))  # [2]

nums = [1, 2, 2]
k = 2
print(s.topKFrequent(nums, k))  # [1,2]

