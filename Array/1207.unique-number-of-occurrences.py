from typing import List


class Solution:
    def uniqueOccurrencesV2(self, arr: List[int]) -> bool:
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
    
    def uniqueOccurrences(self, arr):
        d, ans = {}, []
        for n in arr:
            if n not in d: 
                d[n] = 1
            else: 
                d[n] += 1
        for n in d: 
            ans.append(d[n])
        
        return sorted(ans) == sorted(set(ans))
solution = Solution()
print(solution.uniqueOccurrences([1,2]))