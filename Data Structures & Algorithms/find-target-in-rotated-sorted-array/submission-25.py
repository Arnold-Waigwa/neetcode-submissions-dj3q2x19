class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two scenarios here:
        #1, either the left side is sorted i.e nums[mid] > nums[0]
        #In this case, check if the target is in the range nums[0] < target < nums[mid]
        #if not, check the right side
        #2, The left portion isn't sorted i.e nums[mid] < nums[0]. 
        # This means the right portion is sorted, and we want to check: nums[mid] < target < nums[-1]
        #Else, we check the right side i.e move the binary search pointers to the left portion
        #Last scenario: target isn't    [3,1,1].  target 3
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
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
        