from typing import List

import copy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = candidates
        self.recurse(0, [], target)
        return self.res

    def recurse(self, index, arr, target):
        if target == 0:
            self.res.append(copy.deepcopy(arr))
        if target < 0:
            return
        for i in range(index, len(self.candidates)):
            arr.append(self.candidates[i])
            self.recurse(i, arr, target - self.candidates[i])
            arr.pop()


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]
print(s.combinationSum([2, 3, 5], 8))  # [[2,2,2,2],[2,3,3],[3,5]]
print(s.combinationSum([2], 1))  # []
