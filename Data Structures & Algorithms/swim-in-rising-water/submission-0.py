class Solution:
    import heapq
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        we'll maintain a priority queue for djisktras to use shortes path to that node
        use bfs for traversal, visiting neighbors
        keep visited set to prevent revisiting nodes
        two scenarios:
            valid neighbor; node >= neighbor, add to heap as such (t + 0, node)
            insufficient neigbor; node < neighbor, addtoheap((Node2 - Node1) + t, node)
        track global variable time to return at the end
        """
        #initializations
        neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        min_heap = [(grid[0][0],(0, 0))]
        visited = {(0,0)}
        t = 0
        rows, cols = len(grid), len(grid[0])
        end = (rows - 1, cols - 1)
        #traversing the grid
        #at the end of the grid 
        while True:
            weight, node = heapq.heappop(min_heap)
            t = weight
            if node == end:
                return t
            #inspect neighbors
            row, col = node
            for dr, dc in neighbors:
                nr, nc = dr + row, dc + col
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols  or (nr, nc) in visited): continue
                nei = grid[nr][nc]
                if t >= nei:
                    heapq.heappush(min_heap, (t, (nr, nc)))
                    visited.add((nr, nc))
                else:
                    heapq.heappush(min_heap, (nei, (nr, nc)))
                    visited.add((nr, nc))

        