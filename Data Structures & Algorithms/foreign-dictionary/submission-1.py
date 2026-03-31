from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #create edge list
        graph = defaultdict(list)
        for s in words:
            for c in s:
                graph[c]

        #scan through the list and check pair by pair
        #and k:v the first differing character
        #edge case checks if for two strings that are equal to 
        #the smallest string length, and long comes before short
        for i in range(len(words) - 1):
            a, b = words[i], words[i+1]
            #check edge case
            len_a, len_b = len(a), len(b)
            length = min(len_a, len_b)
            if (a[:length] == b[:length]) and len_a > len_b:
                return ""
            for j in range(length):
                if a[j] != b[j]:
                    graph[a[j]].append(b[j])
                    break
            
        #complete graph, do topological sort
        visited, cycle = set(), set()
        res = []
        def dfs(node: str):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            res.append(node)
            cycle.remove(node)
            visited.add(node)
            return True 

        for key in graph:
            if key not in visited:
                if not dfs(key):
                    return ""

        res.reverse()
        return "".join(res)










