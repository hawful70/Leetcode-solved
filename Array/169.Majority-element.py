class Solution(object):
    def majorityElement(self, nums):
        frequency = {}
        n = len(nums)
        ans = 0
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
                
        for num in nums:
            if frequency[num] > (n / 2):
                ans = num
        return ans
    
    def majorityElementV2(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]
    

solution = Solution()
print(solution.majorityElementV2([2,2,1,1,1,2,2]))
