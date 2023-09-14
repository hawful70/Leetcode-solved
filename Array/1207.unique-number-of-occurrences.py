from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_number, frequency = set(), {}

        for element in arr:
            if element not in frequency:
                frequency[element] = 1
            else:
                frequency[element] += 1

        for element in frequency:
            if frequency[element] not in unique_number:
                unique_number.add(frequency[element])
            else:
                return False
        
        return True
solution = Solution()
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))