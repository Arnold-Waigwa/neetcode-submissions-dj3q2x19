class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        # [0, 1, 2, 3, 4, 5]
        rank = [1] * n
        # [1, 1, 1, 1, 1, 1]

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
            if union(u, v):
                n -= 1
        
        return n
            