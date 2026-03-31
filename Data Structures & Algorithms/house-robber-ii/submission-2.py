class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def dfs(i, memo, num):
            if i >= len(num):
                return 0
            
            if i in memo:
                return memo[i]
            
            #rob
            rob = num[i] + dfs(i + 2, memo, num)

            #skip
            skip = dfs(i+1, memo, num)

            ans = max(rob, skip)
            memo[i] = ans

            return ans
        
        #with first
        memo1, nums1 = {}, nums[:-1]
        first = dfs(0, memo1, nums1)

        #with second
        memo2, nums2 = {}, nums[1:]
        second = dfs(0, memo2, nums2)

        #compare
        return max(first, second)
