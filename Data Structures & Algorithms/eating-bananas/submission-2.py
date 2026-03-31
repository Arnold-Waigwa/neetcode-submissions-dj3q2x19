import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = max(piles)
        l, r = 1, minimum
        while l <= r:
            mid = (l+r) // 2 
            bucket = 0
            for pile in piles:
                bucket += math.ceil(pile/mid)
            if bucket <= h:
                minimum = min(minimum, mid)
                r = mid - 1
            else:
                l = mid + 1
        return minimum
            


        