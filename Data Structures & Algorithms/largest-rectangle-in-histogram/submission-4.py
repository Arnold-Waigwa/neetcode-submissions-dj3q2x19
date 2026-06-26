class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i, height in enumerate(heights):
            ide = i
            while stack and height < stack[-1][1]:
                idx, h = stack.pop()
                area = (i - idx) * h
                largest = max(largest, area)
                ide = idx
            stack.append((ide, height))
        
        while stack:
            idx, h = stack.pop()
            area = (len(heights) - idx) * h
            largest = max(largest, area)
        return largest


