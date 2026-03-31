from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        tickets.sort()

        for v, e in tickets:
            graph[v].append(e)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in graph:
                return False
            
            temp = graph[src]
            for i, v in enumerate(temp):
                graph[src].pop(i)
                res.append(v)

                if dfs(v): return True
                graph[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res




