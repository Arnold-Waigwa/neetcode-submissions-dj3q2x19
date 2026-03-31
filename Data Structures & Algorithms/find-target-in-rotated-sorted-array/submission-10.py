class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if mid > left:
        # we can check if the target is bigger than left
        #and bigger than left, check the left side
        #if mid. is bigger than left but target is smaller than,
        # left, check the right side
        #if mid < left,
        #if mid < left, and target < left, check the left side
        #if mid < left and target > left, check the right side
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1