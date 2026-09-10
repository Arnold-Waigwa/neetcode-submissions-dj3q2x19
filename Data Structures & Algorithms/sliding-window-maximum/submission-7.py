from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        largest = []

        for i, num in enumerate(nums):
            heappush(largest, (-num, i))
            if i >= k - 1:
                while largest[0][1] < i - k + 1:
                    heappop(largest)
                
                res.append(-largest[0][0])

        return res



