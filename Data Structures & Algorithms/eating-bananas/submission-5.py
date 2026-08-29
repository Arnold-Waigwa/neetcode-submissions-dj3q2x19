class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canComplete(rate):
            time = 0

            for pile in piles:
                time += math.ceil(pile / rate)

                if time > h:
                    return False

            return True

        while l < r:
            mid = (l + r) // 2

            if canComplete(mid):
                r = mid
            else:
                l = mid + 1

        return r

