class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if the previous number is bigger, then it is the smallesst
        # if the number before < mid and the first number
        # is > mid, check the left side(the smallest has to be
        #on the left side because it hasn't been reached yet) 
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
            

        

            

