from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        m = len(potions)
        potions.sort()

        def lowerBound(potions, spellElement, target):
            left = 0
            right = len(potions) - 1
            ans = len(potions)

            while left <= right:
                mid = (left + right) // 2
                if potions[mid] * spellElement >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        
        for i in range(len(spells)):
            lowerBoundIndex = lowerBound(potions, spells[i], success)
            lowerBoundIndex = m - lowerBoundIndex
            ans.append(lowerBoundIndex)

        return ans

solution = Solution()
print(solution.successfulPairs([15,8,19], [38,36,23], 328))


    