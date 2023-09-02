class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        f = 0

        while i < len(t) and f < len(s):
            if t[i] == s[f]:
                f += 1
            i += 1

        return f == len(s)        

solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))
print(solution.isSubsequence("axc", "ahbgdc"))