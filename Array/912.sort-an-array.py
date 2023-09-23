import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.selectionSort(nums)
        # self.mergeSort(nums)
        self.quickSort(nums)
        return nums        

    def selectionSort(self, nums: List[int]) -> None:
        n = len(nums)
        currentIndex = 0

        while currentIndex < n:
            minIndex = currentIndex
            for i in range(minIndex + 1, n):
                if nums[i] < nums[minIndex]:
                    minIndex = i
            
            nums[currentIndex], nums[minIndex] = nums[minIndex], nums[currentIndex]
            currentIndex += 1

    def mergeSort(self, nums: List[int]) -> None:
        if len(nums) > 1:
            # split array into 2 parts: left array and right arrays
            n = len(nums)
            mid = n // 2
            left = nums[:mid]
            right = nums[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            # merge left array and right array into 1 part
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

    def quickSort(self, nums: List[int]) -> None:
        def helper(head, tail):
            if head >= tail: 
                return 
            l, r = head, tail
            
            m = random.randint(l,r)
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot: 
                    l += 1
                while r >= l and nums[r] > pivot: 
                    r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)


solution = Solution()
print(solution.sortArray([5,1,1,2,0,0]))

    
        