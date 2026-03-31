from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #first initialize the defaultdict to store the graph
        #go through every edge, edge by edge
        #add it to the graph, run dfs to see if it return a cycle,
        #if it does contain a cycle, return the pair; otherwise, continue
        adjacency_list = defaultdict(list)
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
            visited.remove(node)
            return True      

        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            if not dfs(-1, u):
                return [u, v]


        