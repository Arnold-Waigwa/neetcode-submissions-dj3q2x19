from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        """
        n = len(senate)
        rq = deque()
        dq = deque()

        for i, char in enumerate(senate):
            rq.append(i) if char == "R" else dq.append(i)
        
        while rq and dq:
            if rq[0] < dq[0]:
                new_r, _ = rq.popleft(), dq.popleft()
                rq.append(new_r + n)
            else:
                new_d, _ = dq.popleft(), rq.popleft()
                dq.append(new_d + n)
        
        return "Radiant" if rq else "Dire"



