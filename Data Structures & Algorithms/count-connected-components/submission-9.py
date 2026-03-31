class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * (n)

        #finds the parent of a node
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        #unions two nodes if different parents
        def union(u, v):
            par_u, par_v = find(u), find(v)

            if par_u == par_v:
                return False
            
            if rank[par_u] >= rank[par_v]:
                parent[par_v] = par_u
                rank[par_u] += 1
            else:
                parent[par_u] = par_v
                rank[par_v] += 1

            return True
        
        for e, v in edges:
            if union(e, v):
                n -= 1
        
        return n 
