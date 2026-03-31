class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_Area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                width = i - index
                max_Area = max(max_Area, (height * width))
                start = index
            stack.append([start, h])

        #at this point the stack is either empty or everything has 
        #been extended
        if stack:
            for i in range(len(stack)-1, -1, -1):
                max_Area = max(max_Area, ((len(heights)-stack[i][0])*stack[i][1]))
        
        return max_Area


