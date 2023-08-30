class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        resultOfDivide = []
        calculation = 0
        temp = x
        while temp > 0:
            quotient, remainder = divmod(temp, 10)
            resultOfDivide.append(remainder)
            calculation += 1
            temp = quotient

        ans = 0
        for i in range(len(resultOfDivide)):
            ans += resultOfDivide[i]*pow(10, calculation - 1 - i)

        if ans == x:
            return True
        else:
            return False
        
    def isPalindromeV2(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
            return False
        
        result = 0
        while x > result:
            print(x % 10)
            result = result * 10 + x % 10
            x = x // 10
            
        return True if (x == result or x == result // 10) else False
    
    def isPalindromeV3(self, x: int) -> bool:
        if x<0:
            return False

        inputNum = x
        newNum = 0
        while x>0:
            newNum = newNum * 10 + x%10
            x = x//10
        return newNum == inputNum



solution = Solution()
print(solution.isPalindromeV2(121))
            
