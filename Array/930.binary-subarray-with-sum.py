from typing import Collection, List


class Solution:
    def numSubarraysWithSumV2(self, nums: List[int], goal: int) -> int:
        seen = Collection.defaultdict(int)
        seen[0] = 1
        prefixSum = 0
        ans = 0

        for i in range(len(nums)):
            prefixSum += nums[i]

            if prefixSum - goal in seen:
                ans += seen[prefixSum - goal]

            if prefixSum in seen:
                seen[prefixSum] += 1
            else:
                seen[prefixSum] = 1

        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(S) -> int:
            left, right = 0, 0
            ans = 0
            n = len(nums)
            prefixSum = 0

            while right < n:
                prefixSum += nums[right]

                while prefixSum > S:
                    prefixSum -= nums[left]
                    left += 1
                
                ans += right - left + 1
                right += 1
            return ans
        return atMost(goal) - atMost(goal - 1)
    
solution = Solution()
print(solution.numSubarraysWithSum([0,0,0,0,0], 0))
