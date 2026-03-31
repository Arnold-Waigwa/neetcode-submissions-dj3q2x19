from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #need to make sure no cycles; fully connected
        if len(edges) >= n:
            return False

        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjacency_list[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
      
        return dfs(0, -1) and len(list(visited)) == n 

        
