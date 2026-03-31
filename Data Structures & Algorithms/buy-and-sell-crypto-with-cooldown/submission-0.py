class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        #we'll track the following state (have_coin: bool, profit: int, can_sell: bool)
        
        def dfs(i, have_coin):
            if (i, have_coin) in cache:
                return cache[(i, have_coin)]
            if i >= len(prices):
                return 0
            
            #coin available for sale: have coin; case sell
            if have_coin:
                #sell or keep for better time
                #sell and make profit, then proceed after the cooldown
                sell = prices[i] + dfs(i + 2, False)

                #keep and retain cash
                keep = dfs(i + 1, True)
                cache[(i, have_coin)] = max(keep, sell)            
            else:
                #opportunity to buy or not buy based on preference
                buy = -prices[i] + dfs(i + 1, True)

                skip = dfs(i + 1, False)
                cache[(i, have_coin)] = max(buy, skip)
            
            return cache[(i, have_coin)]

        return dfs(0, False)


    
            

                
                

                    


