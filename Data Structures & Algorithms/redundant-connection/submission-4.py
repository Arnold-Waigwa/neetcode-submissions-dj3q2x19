class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #disjoint set union: union-find
        N = len(edges) + 1
        par = [i for i in range(N)]
        rank = [1] * N

        def find(node):
            if par[node] != node:
                par[node] = find(par[node])
            return par[node]
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                return False

            if rank[root1] < rank[root2]:
                par[root1] = root2
                rank[root2] += 1
            else:
                par[root2] = root1
                rank[root1] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
 