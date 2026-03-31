from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        mapper = defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                key = w[:i] + "*" + w[i+1:]
                mapper[key].append(w)
        
        q = deque([beginWord])
        visited = set([beginWord])

        count = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    key = word[:i] + "*" + word[i+1:]
                    for nei in mapper[key]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            count += 1
        return 0



        
