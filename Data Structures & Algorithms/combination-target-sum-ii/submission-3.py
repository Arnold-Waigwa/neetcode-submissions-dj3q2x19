class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, comb, total):
            if total == target:
                res.append(comb.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            comb.append(candidates[i])
            dfs(i+1, comb, total + candidates[i])


            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            
            comb.pop()
            dfs(j, comb, total)
        
        dfs(0, [], 0)
        return res

            
            