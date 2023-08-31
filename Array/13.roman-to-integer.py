class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        
        diction = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        i = 0
        ans = 0
        n = len(s)

        while i < n:
            if (i + 1 < n and (s[i] + s[i + 1]) in diction):
                ans += diction[s[i] + s[i + 1]]
                i += 2
            else:
                ans += diction[s[i]]
                i += 1
                if i == n - 1:
                    ans += diction[s[i]]
                    return ans
                
        return ans
    
solution = Solution()
#print(solution.romanToInt("III"))
# print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MDCXCV"))
            

        

