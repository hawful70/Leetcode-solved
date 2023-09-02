from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        return str1[0: gcd(len(str1), len(str2))]

solution = Solution()
print(solution.gcdOfStrings("ABABAB", "ABAB"))