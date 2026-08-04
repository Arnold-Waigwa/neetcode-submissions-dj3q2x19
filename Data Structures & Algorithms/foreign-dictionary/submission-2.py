from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)

        for word in words:
            for char in word:
                graph[char]

        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            length = min(len(first), len(second))

            if first[:length] == second[:length]:
                if len(first) > len(second):
                    return ""
                continue

            for j in range(length):
                if first[j] != second[j]:
                    graph[second[j]].append(first[j])
                    break

        res = []
        visited = set()
        visiting = set()

        def dfs(char):
            if char in visiting:
                return False
            if char in visited:
                return True

            visiting.add(char)

            for nei in graph[char]:
                if not dfs(nei):
                    return False

            visiting.remove(char)
            visited.add(char)
            res.append(char)

            return True

        for char in graph:
            if not dfs(char):
                return ""

        return "".join(res)