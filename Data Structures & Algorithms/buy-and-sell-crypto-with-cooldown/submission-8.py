class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = not_holding = cool_down_not_holding = 0
        for i in range(len(prices) - 1, -1, -1):
            temp = not_holding
            #no stock
            #buy/skip
            not_holding = max(-prices[i] + holding, not_holding)
            #have stock
            #sell / keep
            holding = max(holding, prices[i] + cool_down_not_holding)
            
            cool_down_not_holding = temp
        
        return not_holding



        