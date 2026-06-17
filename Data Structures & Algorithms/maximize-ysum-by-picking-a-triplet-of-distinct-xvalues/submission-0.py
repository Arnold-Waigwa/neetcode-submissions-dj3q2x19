class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mp = {}

        for i in range(len(x)):
            if x[i] not in mp:
                mp[x[i]] = y[i]

            mp[x[i]] = max(mp[x[i]], y[i])

        return -1 if len(mp) < 3 else sum(sorted(list(mp.values()))[-3:])