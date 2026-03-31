from collections import defaultdict 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #we can add edges progressively use union find
        #and the first edge with the same parent are the culprit
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n+1)

        def find(node):
            if par[node] != node:
                par[node] = find(par[node])
            return par[node]     

        def union(u, v):
            par_u, par_v = find(u), find(v)
            if par_u == par_v:
                return False
            
            if rank[par_u] > rank[par_v]:
                par[par_v] = par_u
                rank[par_u] += 1
            
            else:
                par[par_u] = par_v
                rank[par_v] += 1

            return True


        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        
