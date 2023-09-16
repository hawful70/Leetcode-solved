from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum, right_sum, left_sum_array, right_sum_array = 0, 0, [0] * n, [0] * n

        for i in range(1, n):
            left_sum += nums[i - 1]
            left_sum_array[i] = left_sum
                
        for i in range(n - 2, -1, -1):
            right_sum += nums[i + 1]
            right_sum_array[i] = right_sum

        for i in range(n):
            if left_sum_array[i] == right_sum_array[i]:
                return i
        return -1
    
    def pivotIndexV2(self, nums: List[int]) -> int:
        left_sum = 0
        sum_array = sum(nums) 

        for index, num in enumerate(nums):
            if left_sum * 2 + num == sum_array:
                return index
            left_sum += num
        return -1



                