class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #recursively
        def binarySearch(l, r):
            if l > r:
                return -1
            
            mid = (l+r) // 2
            if nums[mid] > target:
                return binarySearch(l, mid-1)

            elif nums[mid] < target:
                return binarySearch(mid+1, r)

            else:
                return mid
        return binarySearch(0, len(nums)-1)


        