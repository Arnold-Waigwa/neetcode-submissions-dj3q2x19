class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #we don't want there to be duplicates
        #sort the array
        #check for duplicates at the start by saying if this number 
        #is equal to the prev, continue.
        #do a two sum in the inner loop
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                added = nums[i] + nums[j] + nums[k] 
                if added > 0:
                    k -= 1
                elif added < 0:
                    j += 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j<k:
                        j += 1
        return output

                


                    
