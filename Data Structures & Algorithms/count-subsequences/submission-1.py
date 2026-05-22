class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        
        """go step by step comparing the index of s(j):bigger with that of t(i):smaller
        for each comparison, if s(bigger) is not equal to t(smaller), move its pointer 
        forward for next comparison
        if both are equal, we could either choose to pick it, or move the pointer. 
        this is a branch out, we consider both possibilites
        for each state i,j, we save in
         a cache to prevent recompute and linearizing the complexity
         base case: if we've reached end of smaller one, everything was satisfied
         and we return 1. If we reach end of bigger one without finishing smaller
         , we were unable to find valid sequence, hence return 0
         """
        
        cache = {}
        def dfs(i, j) -> int:
            if (i, j) in cache:
                return cache[(i, j)]

            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            #if comparison isn't matched, move the bigger one to look for valid subsequence
            if s[i] != t[j]:
                cache[(i, j)] = dfs(i + 1, j)
                return cache[(i, j)]
            
            else:
                #if comparison matches, we branch out
                take = dfs(i + 1, j + 1)
                pas = dfs(i + 1, j)
                cache[(i, j)] = take + pas
                return cache[(i, j)]
        
        return dfs(0, 0)
     
                









            
            