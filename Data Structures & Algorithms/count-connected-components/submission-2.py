class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #build parents array
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            if par[node] != node:
                par[node] = find(par[node])
            return par[node]

        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return False

            if rank[par1] < rank[par2]:
                par[par1] = par2
                rank[par2] += 1
            else:
                par[par2] = par1
                rank[par1] += 1
            return True
            
        for u, v in edges:
            if union(u, v):
                n -= 1
        
        return n
