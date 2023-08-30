from functools import lru_cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @lru_cache(None)
        def minCost(n: int):
            if n == 0 or n == 1:
                return cost[n]
            
            return cost[n] + min(minCost(n - 1), minCost(n - 2))
        
        n = len(cost)
        return min(minCost(n - 1), minCost(n - 2))
    

    
solution = Solution()
print(solution.minCostClimbingStairs([10,15,20]))