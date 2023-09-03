from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenFlowbed = len(flowerbed)

        if n == 0:
            return True

        if lenFlowbed == 1 and flowerbed[0] == 1:
            return False
        if lenFlowbed == 1 and flowerbed[0] == 0:
            return True

        for i in range(lenFlowbed):
            if n == 0:
                break
            
            if i == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i == lenFlowbed - 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            
            
        return n == 0
    
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1,0,0], 2))
