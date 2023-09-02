class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowels(s): 
            if (s == 'a' or s == 'e' or s == 'i' or 
                s == 'o' or s == 'u' or s == 'A' or 
                s == 'E' or s == 'I' or s == 'O' or 
                s == 'U'):
                return True
            else:
                return False
            
        left = 0
        right = len(s) - 1

        my_str = list(s)

        while left < right:
            if isVowels(my_str[left]) and isVowels(my_str[right]):
                my_str[left], my_str[right] = my_str[right], my_str[left]

                left += 1
                right -= 1
            elif isVowels(my_str[left]) and not isVowels(my_str[right]):
                right -= 1
            elif not isVowels(my_str[left]) and isVowels(my_str[right]):
                left += 1 
            else:
                right -= 1
                left += 1

            
        return ''.join(my_str)
    
solution = Solution()
print(solution.reverseVowels("leetcode"))