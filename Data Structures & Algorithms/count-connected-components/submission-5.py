from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #going to build our adjacency_list
        #initiazlie our visited list
        #dfs traverse and add visited nodes to visited
        #loop through until n, if i isnt in the set, add n + 1
        #return after the loop the nodes
        adjacency_list = defaultdict(list)

        for edge, vertice in edges:
            adjacency_list[edge].append(vertice)
            adjacency_list[vertice].append(edge)
        
        visited = set()
        def dfs(parent, node):
            visited.add(node)
            for nei in adjacency_list[node]:
                if nei not in visited:
                    dfs(node, nei)
        
        nodes = 0
        for i in range(n):
            if i not in visited:
                nodes += 1
                dfs(-1, i)

        return nodes



        