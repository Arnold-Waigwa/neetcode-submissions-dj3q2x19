class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #start the left at 0 and right at 1
        #get the max profit, which starts at 0
        #if right > left, move left to right otherwise keep going
        max_profit = 0
        l = 0
        for r in range(1,len(prices)):
            max_profit = max(max_profit, prices[r]-prices[l])
            if prices[r] <= prices[l]:
                l = r
        return max_profit

