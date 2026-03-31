class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for j in range(2):
                #0 is you have coins to sell
                if j == 0:
                    #if we sell, we can only buy after cooldown(i+2), but get to keep profit
                    sell = prices[i] + result[i + 2][1] #check false state cause you have no coins after sale
                    #if you hold, you get no profit but retain coin
                    hold = result[i + 1][0] #check true state cause you have coins, but receive no profit
                    result[i][j] = max(sell, hold)
                else:
                    #you have no coins to sell; can buy or pass
                    buy = -prices[i] + result[i + 1][0] #true case as you have get coins by buying
                    skip = result[i + 1][1] #you passed, so no coins but no loss 
                    result[i][j] = max(buy, skip)
        
        return result[0][1] #I start with no coins to sell
