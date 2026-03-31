import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_list = defaultdict(list)
        for u, v, w in times:
            adjacency_list[u].append((w, v))
        
        visited = set()
        pq = [(0, k)]
        time = 0
        while pq:
            if len(visited) == n:
                return time
            w, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            time = w
            for w, v in adjacency_list[node]:
                if v not in visited:
                    heapq.heappush(pq, (time + w, v))
                    
        
        return time if len(visited) == n else -1 