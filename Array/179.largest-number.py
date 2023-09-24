import random
from typing import List


class Solution:
    def compare(self, num1, num2):
        return str(num1) + str(num2) > str(num2) + str(num1)
    
    def selectionSort(self, nums: List[int]):
        n = len(nums)
        currentIndex = 0
        while currentIndex < n:
            maxIndex = currentIndex
            for i in range(currentIndex + 1, n):
                if not self.compare(nums[maxIndex], nums[i]):
                    maxIndex = i
                    
            nums[currentIndex], nums[maxIndex] = nums[maxIndex], nums[currentIndex]
            currentIndex += 1

        return str(int("".join(map(str, nums))))
    
    def quickSort(self, nums, l, r):
        if l >= r:
            return 
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos-1)
        self.quickSort(nums, pos+1, r)
    
    def partition(self, nums, l, r):
        max = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[max] = nums[max], nums[l]
                max += 1
            l += 1
        nums[max], nums[r] = nums[r], nums[max]
        return max

    def largestNumber(self, nums: List[int]) -> str:
        # ans = self.selectionSort(nums)
        self.quickSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums)))) 

    
solution = Solution()
print(solution.largestNumber([3,30,34,5,9]))
