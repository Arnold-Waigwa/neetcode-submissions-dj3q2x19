class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        l, r = 0, 1
        while  r < len(prices):
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                maximum = max(maximum, prices[r] - prices[l])
                r += 1
        return maximum

        