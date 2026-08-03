from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        conduct a dfs, and iterate over all neighbors from the last
        Once a neighbor returns, pop it, and postfix record the node
        """
        tickets.sort(reverse=True)

        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)

        res = []
        def dfs(node):
            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)
            res.append(node)

        dfs('JFK')
        return res[::-1]
    

