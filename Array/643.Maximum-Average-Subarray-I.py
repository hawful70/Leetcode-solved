from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currentSum += nums[i] - nums[i - k]
            maxSum = max(currentSum, maxSum)
        

        return maxSum / k