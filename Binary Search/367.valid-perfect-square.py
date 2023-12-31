class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num


        while left <= right:
            mid = (right + left) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1

        return False
    
solution = Solution()
print(solution.isPerfectSquare(14))
