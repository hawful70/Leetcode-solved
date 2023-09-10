from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        def findMinimum(nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if (mid == left or nums[mid-1] > nums[mid]) and (mid == right or nums[mid] < nums[mid+1]):
                    return mid
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        n = len(nums)
        if n == 1 and nums[0] == target:
            return 0
        
        minimumIndex = findMinimum(nums)

        if minimumIndex == 0:
            return binarySearch(nums, 0, len(nums) - 1, target)
        if minimumIndex == (n - 1):
            if nums[minimumIndex] == target:
                return minimumIndex
        
        if target > nums[n - 1]:
            return binarySearch(nums, 0, minimumIndex - 1, target)
        else:
            return binarySearch(nums, minimumIndex, len(nums) - 1, target)
        
        
        
    
solution = Solution()
print(solution.search([1,2,3,4,5,6,7,0], 3))


    