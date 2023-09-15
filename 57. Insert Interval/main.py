from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        start = 0
        end = 1
        prev = intervals[0]
        res = []
        for curr in intervals:
            if curr[end] < newInterval[start]:
                res.append(curr)
            elif newInterval[start] <= curr[end]:
                newInterval[start] = min(curr[start], newInterval[start])
                newInterval[end] = max(curr[end], newInterval[end])
            elif newInterval[end]<curr[start]:
                res.append(newInterval)
            else:
                res.append(curr)  
        return res


s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5]))  # [[1,5],[6,9]]
print(
    s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
)  # [[1,2],[3,10],[12,16]]
print(s.insert([], [5, 7]))  # [[5,7]]
print(s.insert([[1, 5]], [2, 3]))  # [[1,5]]
print(s.insert([[1, 5]], [2, 7]))  # [[1,7]]
print(s.insert([[1, 5]], [6, 8]))  # [[1,5],[6,8]]
print(s.insert([[1, 5]], [0, 3]))  # [[0,5]]
