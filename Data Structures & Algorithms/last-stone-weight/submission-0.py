import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #convert stones into a heap
        #while loop until len of stones in 1 or 0
        #in the loop, we get the two largets stones
        #crash them following the constraints
        #we return it if theres anything to return
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x,y = -heapq.heappop(stones), -heapq.heappop(stones)

            if x > y:
                z = x - y
                heapq.heappush(stones, -z)
        
        return -stones[0] if stones else 0
            

