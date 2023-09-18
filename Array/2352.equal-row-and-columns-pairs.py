from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = columns = len(grid)
        ans = 0
        hash_sum = defaultdict(int)

        for i in range(len(grid)):
            strArr = str(grid[i])
            hash_sum[strArr] += 1
                
        
        for i in range(columns):
            arrCol = []
            for j in range(rows):
                arrCol.append(grid[j][i])
            
            strArr = str(arrCol)
            ans += hash_sum[strArr]
                

        return ans
solution = Solution()
print(solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))

