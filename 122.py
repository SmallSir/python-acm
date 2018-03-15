class Solution:
    def maxProfit(self, prices):
        cnt = 0
        if len(prices) == 0:
            return cnt
        min_price = prices[0]
        for i in range(len(prices)):
            if i == 0:
                continue
            if prices[i] > prices[i-1]:
                cnt += prices[i] - prices[i-1]
        return cnt