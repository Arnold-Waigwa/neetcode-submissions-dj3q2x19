class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        temperatures = list(zip(range(n), temperatures))
        stack = []
        
        for idx, temp in temperatures:
            while stack and temp > stack[-1][1]:
                i, _ = stack.pop()
                res[i] = idx - i
            
            stack.append((idx, temp))
        
        return res