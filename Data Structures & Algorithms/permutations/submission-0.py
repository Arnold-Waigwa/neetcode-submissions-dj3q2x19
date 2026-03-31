class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(permutation):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in permutation:
                    continue
                #add it
                permutation.append(nums[i])
                dfs(permutation)
                #pop it
                permutation.pop()
        dfs([])
        return result


            
             
                
                

        