class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next1 = [0, 0]
        next2 = [0, 0]

        for i in range(len(prices) - 1, -1, -1):
            curr = [0, 0]
            curr[0] = max(prices[i] + next2[1], next1[0])
            curr[1] = max(-prices[i] + next1[0], next1[1])
            next2 = next1
            next1 = curr
        
        return next1[1]