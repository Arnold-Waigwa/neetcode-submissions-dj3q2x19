class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, combination, total):
            if total == target:
                result.append(combination[:])
                return
            if i >= len(nums) or total > target:
                return
            
            #decision left, add num
            combination.append(nums[i])
            dfs(i, combination, total + nums[i])

            #decision right, no adding num
            combination.pop()
            dfs(i+1, combination, total)

        dfs(0, [], 0)
        return result




