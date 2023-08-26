# idea: find pair prices[left] and prices[right] such that prices[left] < prices[right], then calculate sum of all pairs

class Solution(object):
    def maxProfit(self, prices):
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxProfit += prices[right] - prices[left]
            left += 1
            right += 1
        
        return maxProfit