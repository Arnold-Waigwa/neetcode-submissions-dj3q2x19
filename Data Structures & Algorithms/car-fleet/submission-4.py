class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #have a stack that keeps track of the car fleets
        #We need to sort in order to start from the nearest one and check in
        #descending order
        #store the position and speed together and sort it, and
        #then create the stack.
        #populate the stack by checking if the next car will reach before the previous
        #one. If it does, pop the 
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



        