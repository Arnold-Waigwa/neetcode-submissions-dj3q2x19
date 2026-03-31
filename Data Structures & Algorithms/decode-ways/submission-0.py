class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        def dfs(i):
            nonlocal count
            if i >= len(s):
                count += 1
                return 
            for j in range(i, min(i + 2, len(s))):
                string = s[i:j+1]
                if string[0] == "0" or int(string) > 26:
                    continue
                dfs(j + 1)
        
        dfs(0)
        return count
                

                
                
                

        