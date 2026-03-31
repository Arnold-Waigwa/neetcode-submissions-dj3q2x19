import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #start the binary search from 1 - max(piles)
        #l = 1, r = max(piles)
        #binary search, if mid just needed to keep a min res
        #and compare when l > r
        res = max(piles)
        l, r  = 1, res
        while l <= r:
            mid = (l+r) // 2
            bucket = 0
            for pile in piles:
                if bucket > h:
                    break
                bucket += math.ceil(pile/mid)
            if bucket <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
            
        return res
                

