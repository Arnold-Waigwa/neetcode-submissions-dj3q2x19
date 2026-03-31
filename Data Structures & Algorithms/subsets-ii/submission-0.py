class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        def dfs(i, combination):
            if i == len(nums):
                output.append(combination.copy())
                return
            
            #decision left, add
            combination.append(nums[i])
            dfs(i+1, combination)
            combination.pop()

            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            dfs(j, combination)
        
        dfs(0, [])
        return output


        