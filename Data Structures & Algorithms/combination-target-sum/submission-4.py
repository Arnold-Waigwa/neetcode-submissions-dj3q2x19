class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #go to the same tree again, then if it returns go to the next
        #go to the next tree 
        res = []
        def dfs(i, comb, val):
            if i >= len(nums) or val > target:
                return
            
            if val == target:
                res.append(comb.copy())
                return

            #add this branch until it works or is invalid
            comb.append(nums[i])
            dfs(i, comb, val + nums[i])

            #dont take this branch at all and go play with the next one
            comb.pop()
            dfs(i + 1, comb, val)
        
        dfs(0, [], 0)
        return res




