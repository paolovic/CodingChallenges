from typing import List
import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteHelper(nums, [], [])

    def permuteHelper(
        self, nums: List[int], currList: List[int], result: List[List[int]]
    ) -> List[List[int]]:
        if len(nums) == 0:
            result.append(copy.deepcopy(currList))
        for x in nums:
            currList.append(x)
            cp_nums = copy.deepcopy(nums)
            cp_nums.remove(x)
            self.permuteHelper(cp_nums, currList, result)
            currList.pop()
        return result


s = Solution()
# Test Case 1:
print(
    s.permute([1, 2, 3])
)  # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Test Case 2:
print(s.permute([0, 1]))  # Expected: [[0,1],[1,0]]

# Test Case 3:
print(s.permute([1]))  # Expected: [[1]]

# Test Case 4:
print(s.permute([]))  # Expected: []
