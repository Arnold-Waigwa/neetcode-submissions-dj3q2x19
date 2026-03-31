from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #init adjacencylist
        graph = defaultdict(set)

        for word in words:
            for c in word:
                graph[c]
        #populate graph by comparison and return string early for invalid
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            length = min(len(w1), len(w2))

            if w1[:length] == w2[:length] and len(w1) > len(w2):
                return ""

            #compare c by c
            for j in range(length):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True
            for nei in graph[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            res.append(c)
            return False
        
        for c in graph:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)



