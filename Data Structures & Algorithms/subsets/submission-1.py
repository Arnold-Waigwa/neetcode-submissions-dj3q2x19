class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            #option one
            subset.append(nums[i])
            dfs(i+1, subset)

            #option two
            subset.pop()
            dfs(i+1, subset)
        
        dfs(0, [])
        return res