import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatEnough(piles: List[int], speed, h):
            countingHours = 0

            for pile in piles:
                countingHours += math.ceil(pile / speed)
                
            return countingHours <= h
        
        left = 1
        right = max(piles)
        ans = len(piles)

        while left <= right:
            mid = (left + right) // 2
            if eatEnough(piles, mid, h):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
    
solution = Solution()
print(solution.minEatingSpeed([3,6,7,11], 8))

        