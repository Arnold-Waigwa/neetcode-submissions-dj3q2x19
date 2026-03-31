from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree = undirected, acyclic, connected graph
        #already undirected: need to verify acyclic and connected
        #if edges > nodes, cannot be acyclic
        if len(edges) >= n:
            return False
        
        adjacency_list = defaultdict(list)

        #we have a double relationship(undirected) edge list
        for vert, edge in edges:
            adjacency_list[vert].append(edge)
            adjacency_list[edge].append(vert)
        
        visited = set()
        def dfs(parent, node):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjacency_list[node]:
                if nei == parent:
                    continue
                if not dfs(node, nei):
                    return False
            return True
             
        return dfs(-1, 0) and len(visited) == n
        


