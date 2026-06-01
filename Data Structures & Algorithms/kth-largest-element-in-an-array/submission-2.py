class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heapq.nLargest(nums,k)
        return heapq.nlargest(k, nums)[-1]