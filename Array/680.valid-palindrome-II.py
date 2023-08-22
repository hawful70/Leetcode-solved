class Solution():
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            print(s[0:4])
            if s[left].lower() != s[right].lower():
                return self.isValidPalindrome(s, left, right - 1) or self.isValidPalindrome(s, left + 1, right)
            else:
                left += 1
                right -= 1
        return True

    def isValidPalindrome(self, s, left, right):
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
    
    def validPalindromeV2(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].lower() != s[right].lower():
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]
            else:
                left += 1
                right -= 1
        return True
    
solution = Solution()
print(solution.validPalindromeV2("deddde"))
# print(solution.validPalindromeV2("abceba"))
# print(solution.validPalindromeV2("deead"))
# print(solution.validPalindromeV2("raceacat"))
# print(solution.validPalindromeV2("aba"))
# print(solution.validPalindromeV2("abca"))
# print(solution.validPalindromeV2("abc"))