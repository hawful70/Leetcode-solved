class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = left + 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                if maxProfit < profit:
                    maxProfit = profit
            right += 1
        return maxProfit
    
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))