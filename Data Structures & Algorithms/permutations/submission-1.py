class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(comb):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in comb:
                    comb.append(nums[i])
                    dfs(comb)
                    comb.pop()
        
        dfs([])
        return res
