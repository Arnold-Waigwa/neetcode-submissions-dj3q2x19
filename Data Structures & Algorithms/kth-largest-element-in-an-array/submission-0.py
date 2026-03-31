class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #maintain a heap of size k
        #we'll heapify nums in O(log N)
        #we'll continously remove from the heap until size k, where in
        #we'll find our kth largest in heap[0]
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]