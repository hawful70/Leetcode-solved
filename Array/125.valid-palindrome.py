import re

class Solution():
    def isPalindrome(self, s: str):
        newStr = re.sub(r'[\W_]', '', s)
        newStr = newStr.lower()

        if len(newStr) == 0:
            return True
        
        lenOfStr = len(newStr)
        i = 0
        j = lenOfStr - 1

        while i < j:
            if newStr[i] != newStr[j]:
                return False
            i += 1
            j -= 1
        
        return True
    
    def isPalindromeV2(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            
            while l < r and s[l].isalnum() == False: 
                l += 1
            while r > l and s[r].isalnum() == False: 
                r -= 1
            if l > r or s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
    
solution = Solution()
solution.isPalindromeV2('A man, a plan, a canal: Panama')
