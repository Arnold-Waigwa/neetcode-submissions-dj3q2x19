class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(i, flag):
            if i == len(nums) - 1:
                return max(0, nums[i]) if flag else nums[i]
            if flag:
                return max(0, nums[i] + dfs(i + 1, True))
            return max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
        return dfs(0, False)