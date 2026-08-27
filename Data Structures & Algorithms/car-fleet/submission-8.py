class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        calculate the time cars reach starting from the nearest
        one. A car cannot reach before a car ahead of it, if 
        it does, it's a fleet, pop it
        """
        cars = sorted(list(zip(position, speed)), reverse=True)
        stack = []

        for pos, sp in cars:
            time = (target - pos) / sp

            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)


