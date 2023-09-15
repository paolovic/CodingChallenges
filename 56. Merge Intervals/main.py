from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = 0
        end = 1

        intervals.sort(key=lambda a: a[start])

        prev = intervals[0]
        res = [prev]

        for curr in intervals:
            if curr[start] <= prev[end]:
                prev[end] = max(curr[end], prev[end])
            else:
                res.append(curr)
                prev = curr
        return res


s = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(s.merge(intervals))

intervals = [[1, 4], [4, 5]]
print(s.merge(intervals))
