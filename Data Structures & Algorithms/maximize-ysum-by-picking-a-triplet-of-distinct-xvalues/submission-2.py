import heapq
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        """
        pick the max, check if its valid, and repeat

        """
        pq = [(-y[i], x[i]) for i in range(len(x))]
        heapq.heapify(pq)
        seen = set()
        res = []
        while pq:
            val_y, val_x = heapq.heappop(pq)
            print("y is", val_y)
            print("x is", val_x)
            if val_x in seen:
                continue
            res.append(-val_y)
            seen.add(val_x)
            if len(res) == 3:
                print(res)
                return sum(res)

        return -1
