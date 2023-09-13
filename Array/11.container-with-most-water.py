from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left <= right:
            currentArea = min(height[left], height[right]) * (right - left)
            res = max(currentArea, res)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
