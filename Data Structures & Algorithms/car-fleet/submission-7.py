class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        different positions with goal of reaching target
        each car goes at i speed
        a car from behind can catch up if it goes fast, if there's
        enough distance
        [1, 4] [3, 2] 10
        4, 7, 10 how much time to reach the destination?
        6, 8, 10
        t = 9/3 = 3s
        t = 6/2 = 3s need to be sorted
        """
        acc = [(position[i], speed[i]) for i in range(len(position))]
        acc.sort(reverse=True)
        stack = []

        for pos, sp in acc:
            t = ( target - pos ) / sp
            if len(stack) == 0:
                stack.append(t)
                continue
            if t > stack[-1]:
                stack.append(t)
        return len(stack)
        


