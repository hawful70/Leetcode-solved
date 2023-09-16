from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        left = 0
        right = len(nums) - 1
        operation = 0

        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
               operation += 1
               nums[left] = 0
               nums[right] = 0
               left += 1
               right -= 1
            elif sum < k:
                left += 1
            else:
                right -= 1
        return operation
    
solution = Solution()
print(solution.maxOperations([1,2,3,4], 5))
        
        
            