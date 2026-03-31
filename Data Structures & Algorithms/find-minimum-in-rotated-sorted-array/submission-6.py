class Solution:
    def findMin(self, nums: List[int]) -> int:
        #we always know that if the middle is bigger 
        #than the end, the minimum will be at the right side
        #otherwise, the middle is at the left side
        #[1] once its equal , return it
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else: r = mid
        return nums[l]
        