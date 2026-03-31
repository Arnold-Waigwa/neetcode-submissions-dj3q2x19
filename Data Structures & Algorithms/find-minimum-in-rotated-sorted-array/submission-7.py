class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the middle will always be smaller then the right, and the section 
        #you wanna search in this case is the first half
        #if the middle is greater than the right most, the min will be in the 
        #second section
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid + 1
        return nums[l]
            
