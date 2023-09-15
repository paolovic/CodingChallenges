from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start = 0
        end = 1
        intervals.sort(key=lambda a: a[start])
        prev = intervals[start]

        for i in range(1, len(intervals)):
            if prev[end] >= intervals[i][start]:
                return False
            else:
                prev = intervals[i]
        return True


s = Solution()
print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  # false

print(s.canAttendMeetings([[7, 10], [2, 4]]))  # true
