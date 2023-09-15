from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        count=0
        start = 0
        end = 1
        intervals.sort(key=lambda a: a[start])
        prev = intervals[0]
        for curr in intervals:
            if curr[start]<prev[end]:
                count+=1
                curr[end]=min(curr[end], prev[end])
            prev=curr
        return count


s = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
print(s.minMeetingRooms(intervals))  # 2

intervals = [[7, 10], [2, 4]]
print(s.minMeetingRooms(intervals))  # 1
