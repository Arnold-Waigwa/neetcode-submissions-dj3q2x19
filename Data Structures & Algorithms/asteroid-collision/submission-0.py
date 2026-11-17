class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        maintain a monotonic positive stack
        scan through asteroids
        if asteroid is positive, add it to the stack
        if its negative:
            compare the top of the stack and negative asteroid
            if its smaller, continue. if same size, pop and continue
            otherwise, while its greater, pop from the stack
            if stack is empty, store the negative in results array
        at the end, extend stack to the array
        """
        stack, result = [], []
        for asteroid in asteroids:
            if asteroid >= 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] < abs(asteroid):
                    stack.pop()
                if not stack:
                    result.append(asteroid)
                elif stack and stack[-1] == abs(asteroid):
                    stack.pop()

        result.extend(stack)
        return result

            