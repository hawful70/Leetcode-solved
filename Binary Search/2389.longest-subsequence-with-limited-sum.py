from bisect import bisect_right
from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()

        for i in range(1, len(nums)):
           nums[i] = nums[i] + nums[i - 1]

        for query in queries:
           ans.append(bisect_right(nums, query))

        return ans
    
solution = Solution()
print(solution.answerQueries([2,3,4,5], [1]))


