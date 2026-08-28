class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            idx = i
            while stack and height < stack[-1][1]:
                idx, h = stack.pop()
                max_area = max(max_area, (i - idx) * h)
            
            stack.append((idx, height))
        
        while stack:
            idx, h = stack.pop()
            max_area = max(max_area, (len(heights) - idx) * h)
        
        return max_area
