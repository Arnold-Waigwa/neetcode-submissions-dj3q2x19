from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #essentially want to process the frequent tasks first
        #use a maxheap to pop most frequent tasks
        #store in queue for organization and accessing / adding back
        #to heap for processing
        #keeping time var to store time
        #go through list and get count of every element
        nums = list(Counter(tasks).values())
        nums = [(-n, 0) for n in nums]
        q = deque()
        heapq.heapify(nums)
        time = 0

        while nums or q:
            #at each iteration I want to add into the heap if possible
            if q and q[0][1] == time:
                heapq.heappush(nums, q.popleft())
            
            if nums:
                val, _ = heapq.heappop(nums)
                val += 1
                if val:
                    q.append((val, time + n + 1))
            time += 1
        return time

            


            



        

        

