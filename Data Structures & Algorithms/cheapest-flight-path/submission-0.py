from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #create the edgelist
        graph = defaultdict(list)
        for sr, de, we in flights:
            graph[sr].append([we, de])
        
        min_heap = [[0, src, -1]]

        while min_heap:
            weight, node, stops = heapq.heappop(min_heap)
            if node == dst:
                if stops <= k:
                    return weight
                continue
            
            #if curr not dest, push neighbors to queue appending stops + 1
            for w, nei in graph[node]:
                heapq.heappush(min_heap, [weight + w, nei, stops + 1])
        
        return -1