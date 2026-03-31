class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev):
            if (i, prev) in memo:
                return memo[(i, prev)]
            if i >= len(nums):
                return 0

            exclude = dfs(i + 1, prev)

            include = 0
            if nums[i] > prev:
                include = 1 + dfs(i + 1, nums[i])

            ans = max(include, exclude)
            memo[(i, prev)] = ans
            return ans
        return dfs(0, float("-inf"))


