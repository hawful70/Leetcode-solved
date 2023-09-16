from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        ans = [0] * (n + 1)

        for i in range(1, len(ans)):
            ans[i] = ans[i - 1] + gain[i - 1]
        
        return max(ans)
    
solution = Solution()
print(solution.largestAltitude([-5,1,5,0,-7]))

