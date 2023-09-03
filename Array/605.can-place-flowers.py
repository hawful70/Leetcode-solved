from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenFlowbed = len(flowerbed)

        if n == 0:
            return True

        for i in range(lenFlowbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == lenFlowbed - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
        
    
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1,0,0], 2))
