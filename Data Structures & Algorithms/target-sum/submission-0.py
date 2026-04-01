class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, amt):
            if i == len(nums):
                return amt == target

            if (i, amt) in cache:
                return cache[(i, amt)]

            add = dfs(i + 1, amt + nums[i])
            sub = dfs(i + 1, amt - nums[i])
            cache[(i, amt)] = add + sub

            return cache[(i, amt)]
        
        return dfs(0, 0)
