from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        numberOfDeletingZero = 0

        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                numberOfDeletingZero += 1

            if numberOfDeletingZero > 1:
                if nums[left] == 0:
                    numberOfDeletingZero -= 1
                left += 1

            if numberOfDeletingZero <= 1:
                ans = max(ans, right - left + 1 - numberOfDeletingZero)

        return ans - 1 if ans == len(nums) else ans