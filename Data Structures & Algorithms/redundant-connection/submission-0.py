from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        the key here is to incrementally add edges onto the graph
        and doing dfs to determine if you can reach a cycle with the current
        edges, and if not continue, if so, return those edges
        """
        adjacency_list = defaultdict(list)

        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for neigh in adjacency_list[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node):
                    return True
            return False
        

        for vert, edge in edges:
            adjacency_list[vert].append(edge)
            adjacency_list[edge].append(vert)
            visited = set()
            if dfs(vert, -1):
                return [vert, edge]
        return [] 
