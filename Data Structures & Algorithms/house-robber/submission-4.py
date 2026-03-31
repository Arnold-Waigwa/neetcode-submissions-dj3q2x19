class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, acc):
            if i >= len(nums):
                return acc
            
            if (i, acc) in dp:
                return dp[(i, acc)]
            #rob this house
            amt1 = dfs(i + 2, acc + nums[i])

            #skip this house
            amt2 = dfs(i + 1, acc)

            ans = max(amt1, amt2)
            dp[(i, acc)] = ans
            return ans

        return (dfs(0, 0))

            

            
                

            