class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(i, total):
            if total == target:
                res.append(comb[:])
                return
            
            if i >= len(nums) or total > target:
                return

            #option one
            comb.append(nums[i])
            dfs(i, total + nums[i])

            #option two
            comb.pop()
            dfs(i+1, total)
        
        dfs(0, 0)
        return res
