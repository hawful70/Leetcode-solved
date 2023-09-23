from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return "".join(map(str, nums))
        
        currentIndex = 0
        operation = 0
        while currentIndex < n:
            maxIndex = currentIndex
            for i in range(currentIndex + 1, n):
                strMaxElement = str(nums[maxIndex])
                strCurrentElement = str(nums[i])
                if int(strMaxElement + strCurrentElement) < int(strCurrentElement + strMaxElement):
                    maxIndex = i
                    
            
            nums[currentIndex], nums[maxIndex] = nums[maxIndex], nums[currentIndex]
            if nums[currentIndex] == 0:
                operation += 1
            currentIndex += 1

        if operation == len(nums):
            return str(nums[0])
        return "".join(map(str, nums))
    
solution = Solution()
print(solution.largestNumber([0,9,8,7,6,5,4,3,2,1]))
