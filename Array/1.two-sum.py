class Solution():
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

    def twoSumV2(self, nums, target):
        mapping = {}
        n = len(nums)
        for i in range(n):
            result = target - nums[i]
            if result in mapping:
                return [mapping[result], i]
            mapping[nums[i]] = i
        return []

    
solution = Solution()
print(solution.twoSumV2([3,2,4], 6))

            
            