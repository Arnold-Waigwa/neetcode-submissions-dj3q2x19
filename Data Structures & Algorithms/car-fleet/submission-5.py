class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #combine the two into an array of its position and time
        array = sorted([(position[i], speed[i]) for i in range(len(position))])

        stack = []

        #go through the back and add the tuple in the stack
        for i in range(len(array)-1, -1, -1):
            #calculate the time and add to the stack
            time = (target-array[i][0]) / array[i][1]
            stack.append(time)
            if len(stack) > 1:
                if stack[-1] <= stack[-2]:
                    stack.pop()
            
        return len(stack)
        