class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        memo = {}

        def dfs(i, val):
            if i >= len(nums) or val < 0:
                return False

            if (i, val) in memo:
                return memo[(i, val)]
            
            if val == 0:
                return True
            
            left = dfs(i+1, val - nums[i])
            right = dfs(i+1, val)
            memo[(i,val)] = left or right
            return memo[(i, val)]
            
        
        return dfs(0, target)



       

