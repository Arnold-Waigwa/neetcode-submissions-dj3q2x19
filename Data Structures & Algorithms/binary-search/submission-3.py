class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two pointers
        def binarySearch(l, r):
            mid = (l + r) // 2
            if l > r:
                return -1
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                return binarySearch(l, r-1)

            elif nums[mid] < target:
                return binarySearch(l+1, r)
        
        return binarySearch(0, len(nums)-1)