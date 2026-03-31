class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(i, combination, total):
            if total == target:
                output.append(combination[:])
                return
            
            if i >= len(nums) or total > target:
                return
            
            #decision left
            #add nums[i]
            combination.append(nums[i])
            dfs(i, combination, total + nums[i])

            #decision right
            combination.pop()
            dfs(i + 1, combination, total)
        
        dfs(0, [], 0)
        return output
            

        