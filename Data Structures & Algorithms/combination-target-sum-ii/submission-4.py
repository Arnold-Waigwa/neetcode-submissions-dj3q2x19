class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, comb, val):
            if val == target:
                res.append(comb.copy())
                return
            
            if i >= len(candidates) or val > target:
                return
            
            #pick this branch
            comb.append(candidates[i])
            dfs(i + 1, comb, val + candidates[i])

            comb.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            dfs(i + 1, comb, val)
        
        dfs(0, [], 0)
        return res
            


