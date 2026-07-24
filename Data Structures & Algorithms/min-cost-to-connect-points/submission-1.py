from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)

        # Build adjacency list using indices
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        # Prim's algorithm
        pq = [(0, 0)]  # (cost, node_index)
        visited = set()
        cost = 0

        while len(visited) < n:
            weight, node = heapq.heappop(pq)
            if node in visited:
                continue

            visited.add(node)
            cost += weight

            for edge in graph[node]:
                heapq.heappush(pq, edge)

        return cost
