class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(i, combination, total):
            if total == target:
                result.append(combination[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            #decision to add i .... to n
            
            combination.append(candidates[i])
            dfs(i+1, combination, total + candidates[i])
            #remove the i cause it can start anywhere
            combination.pop()
            #go to the next
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j = j + 1
            dfs(j, combination, total)
        dfs(0, [], 0)
        return result
