class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for ind, height in enumerate(heights):
            start = ind
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                max_area = max(max_area, h * (ind - i))
                start = i
            stack.append((start, height))

        for ind, height in stack:
            max_area = max(max_area, height * (len(heights)-ind))
        
        return max_area

 
        