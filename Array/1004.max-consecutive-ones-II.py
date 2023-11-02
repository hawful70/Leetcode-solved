from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        numberOfZero = 0
        maxNumber = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                numberOfZero += 1

            if numberOfZero > k:
                if nums[left] == 0:
                    numberOfZero -= 1
                left += 1

            if numberOfZero <= k:
                maxNumber = max(maxNumber, right - left + 1)
        
        return maxNumber