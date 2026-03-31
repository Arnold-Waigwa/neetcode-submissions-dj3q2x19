class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            else:
                #start a two sum with nums[i] that adds up to 0
                left, right = i + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total > 0:
                        right -= 1
                    elif total < 0:
                        left += 1
                    else:
                        res.append([nums[i],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while nums[left] == nums[left-1] and left < right:
                            left += 1
        return res
                    

                   
                  
                    


        