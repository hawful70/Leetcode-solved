from functools import lru_cache


class Solution(object):
    def generateV2(self, numRows):
        triangle = []
        
        for i in range(1, numRows + 1):
            item = [0] * i
            item[0] = 1
            triangle.append(item)
        
        i = 1
        k = 1
        while i >= 1 and i <= numRows - 1:
            if k == len(triangle[i]) - 1:
                triangle[i][k] = 1
                i += 1
                k = 1
            else:
                triangle[i][k] = triangle[i - 1][k - 1] + triangle[i - 1][k]
                k += 1

        return triangle

    def generate(self, numRows):
        @lru_cache(None)
        def F(i, j):
            if i == j or j == 0:
                return 1
            return F(i - 1, j - 1) + F(i - 1, j)
        
        ans = []
        for i in range(numRows):
            ans.append([])
            for j in range(i + 1):
                ans[-1].append(F(i, j))
        
        return ans
    
solution = Solution()
print(solution.generate(5))


