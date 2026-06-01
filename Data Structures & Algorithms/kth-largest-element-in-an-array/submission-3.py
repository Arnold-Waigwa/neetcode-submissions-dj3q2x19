import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:]
        heapq.heapify(heap)

        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        return heapq.heappop(heap)
