from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        memo = {}

        def dfs(val, i):
            if val == 0:
                return True
            if val < 0 or i == len(nums):
                return False
            
            if (val, i) in memo:
                return memo[(val, i)]


            include = dfs(val - nums[i], i + 1)

            exclude = dfs(val, i + 1)

            memo[(val, i)] = include or exclude
            return memo[(val, i)]
            
        return dfs(sum(nums) // 2, 0)
