from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patternList = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patternList[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for val in patternList[pattern]:
                        if val not in visited:
                            visited.add(val)
                            q.append(val)
            res += 1
        return 0

        

        