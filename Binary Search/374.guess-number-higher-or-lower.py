class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            ans = guess(mid) 
            if ans == 0:
                return mid
            elif ans == 1:
                left = mid + 1
            else:
                right = mid - 1

        return -1