class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l = 0
        for r in range(1, len(prices)):
            maxprofit = max(maxprofit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return maxprofit

        