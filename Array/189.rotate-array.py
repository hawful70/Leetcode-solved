from typing import List
from collections import deque


class Solution:
    def rotateV2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        while k > 0:
            lastItem = nums[n - 1]
            for i in range(n-2, -1, -1):
                nums[i + 1] = nums[i]
            
            nums[0] = lastItem
            k -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, start, end):
            i = start
            j = end

            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        k = k % len(nums)

        reverse(nums, 0, len(nums) - k - 1)
        reverse(nums, len(nums) - k, len(nums) - 1)  
        reverse(nums, 0, len(nums) - 1)   
        print(nums) 
    

        
            

solution = Solution()
solution.rotate([1,2,3,4,5,6,7], 3)