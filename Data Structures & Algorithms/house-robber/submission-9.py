from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0
            
            take = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)

            return max(take, skip)
        
        
        return max(dfs(0), dfs(1))

            