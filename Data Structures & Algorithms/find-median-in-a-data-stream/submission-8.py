import heapq
class MedianFinder:
    #for the first two, it doesn't matter
    #max heap[1].      min heap[2,3]
    #len = 2              len = 3         median = 2
    #if val > minheap[0] 
    # but if len(minheap) > len(maxheap) do some corrections

    def __init__(self):
       self.minHeap = []
       self.maxHeap = []
       heapq.heapify(self.minHeap)
       heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if not self.minHeap or not self.maxHeap or num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -num)

        else:
            heapq.heappush(self.minHeap, num)

        #clean up
        mx_len = len(self.maxHeap)
        mn_len = len(self.minHeap)
        if abs(mx_len - mn_len) > 1:
            if mx_len > mn_len:
                heapq.heappush(self.minHeap, -(heapq.heappop(self.maxHeap)))
            else:
                heapq.heappush(self.maxHeap, -(heapq.heappop(self.minHeap)))

        
    def findMedian(self) -> float:
        mx_len = len(self.maxHeap)
        mn_len = len(self.minHeap)
        if self.minHeap or self.maxHeap:
            if mx_len == mn_len:
                return (-(self.maxHeap[0]) + self.minHeap[0]) / 2
            elif mx_len > mn_len:
                return -(self.maxHeap[0])
            else:
                return self.minHeap[0]
                

    
        
        