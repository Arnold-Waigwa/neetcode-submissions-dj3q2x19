class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(i, array):
            #base case
            if i == len(nums):
                output.append(array[:])
                return
            #decision left
            array.append(nums[i])
            dfs(i + 1, array)
            array.pop()
            dfs(i + 1, array)
        
        dfs(0, [])
        return output

        