from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        current_solution = []

        def choose(increment = 1):
            if len(current_solution) == k:
                ans.append(current_solution[:])
                return
            
            for i in range(increment, n + 1):
                current_solution.append(i)

                choose(i + 1)

                current_solution.pop()

        choose()
        return ans
    
solution = Solution()
print(solution.combine(4, 2))
