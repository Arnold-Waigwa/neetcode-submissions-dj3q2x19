import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        current time
        time starts at 0, tasks that start at i, then prefer the shortest
        time
        sort with time first
        """
        q = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        
        heapq.heapify(q)
        curr = q[0][0]

        pq = []
        res = []

        while q or pq:
            while q and q[0][0] <= curr:
                enqTime, procTime, index = heapq.heappop(q)
                heapq.heappush(pq, (procTime, index))
            if not pq:
                curr = q[0][0]
                continue

            procTime, index = heapq.heappop(pq)
            curr += procTime
            res.append(index)

        return res      
            



