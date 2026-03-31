from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #distances stored in the heap
        #consider all elements in the loop
        #at the end, use a while loop to pop off k distances
        res = []
        heap = []
        heapq.heapify(heap)
        x1, y1 = 0, 0
        for i in range(len(points)):
            x2, y2 = points[i][0], points[i][1]

            distance = (x2-x1)**2 + (y2-y1)**2

            heapq.heappush(heap, (distance, points[i]))
        
        for _ in range(k):
            _, point = heapq.heappop(heap)
            res.append(point)

        return res




