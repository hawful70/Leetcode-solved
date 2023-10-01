from typing import Collection, List


class Solution:
    def maxOperationsV2(self, nums: List[int], k: int) -> int:
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
    
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Collection.defaultdict(int)
        ans = 0

        for num in nums:
            complement = k - num
            if complement in cnt and cnt[complement] > 0:
                ans += 1
                cnt[complement] -= 1
            else:
                cnt[num] += 1

        return ans