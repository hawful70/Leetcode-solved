from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        ans = []

        for candy in candies:
            if candy + extraCandies >= maxCandy:
                ans.append(True)
            else:
                ans.append(False)

        return ans
    
solution = Solution()
print(solution.kidsWithCandies([4,2,1,1,2], 1))