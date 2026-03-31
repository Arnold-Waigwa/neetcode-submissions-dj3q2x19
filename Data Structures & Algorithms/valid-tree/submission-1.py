import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency_list = collections.defaultdict(list)
        for post, prev in edges:
            adjacency_list[post].append(prev)
            adjacency_list[prev].append(post)
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
            
        return dfs(0, -1) and len(visited) == n
        

