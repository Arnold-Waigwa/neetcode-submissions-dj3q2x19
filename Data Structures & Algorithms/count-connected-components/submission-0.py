from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #create the adjacency list
        adjacency_list = defaultdict(list)
        for node, edge in edges:
            adjacency_list[node].append(edge)
            adjacency_list[edge].append(node)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
            return

        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        
        return components

        