from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, right_array, left_array = [], [1] * len(nums),  [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            if i == 0:
                left_array[0] = 1
            else:
                pre *= nums[i - 1]
                left_array[i] = pre

        sub = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_array[len(nums) - 1] = 1
            else:
                sub *= nums[i + 1]
                right_array[i] = sub
        
        for i in range(len(nums)):
            ans.append(left_array[i] * right_array[i])

        return ans
    
    def productExceptSelfV2(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        pre = 1
        post = 1

        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[length - i - 1] *= post
            post *= nums[length - i - 1]

        return ans
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))