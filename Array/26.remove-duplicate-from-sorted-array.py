class Solution(object):
    def removeDuplicatesV2(self, nums):
        i = k = len(nums) - 1
        n = len(nums)
        found = 0
        visits = set()
        while i >= 0:
            if nums[i] in visits:
                found += 1
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp
                k -= 1
            visits.add(nums[i])
            i -= 1
        i = 0
       
        sorted_list = sorted(visits)
        
        for element in sorted_list:
            nums[i] = element
            i += 1
            if (i > (n - found - 1)):
                break
        return n - found

    def removeDuplicates(self, nums):
        f = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[f - 1]:
                nums[f] = nums[i]
                f += 1
        return f
    
solution = Solution()
print(solution.removeDuplicates(sorted([9,4,9,8,4])))