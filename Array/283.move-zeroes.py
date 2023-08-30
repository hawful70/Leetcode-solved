from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        f = 0

        for i in range(1, n):
            if nums[i] != nums[f] and nums[f] == 0:
                nums[i], nums[f] = nums[f], nums[i]
                f += 1
            if nums[i] != nums[f] and nums[i] == 0:
                f = i
        
solution = Solution()
#solution.moveZeroes([0,1,0,3,12])
solution.moveZeroes([1,0,1])
                


