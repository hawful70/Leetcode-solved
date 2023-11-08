from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        f = 2
        n = len(nums)

        for i in range(2, n):
            if nums[i] != nums[f - 2]:
                nums[f] = nums[i]
                f += 1
        return f