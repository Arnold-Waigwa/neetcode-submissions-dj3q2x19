class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #wanna keep a stack that holds the idx and val
        stack, max_area = [], 0
        for i, h in enumerate(heights):
            curr_i = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                area = (i - idx) * height
                max_area = max(max_area, area)
                curr_i = idx
            stack.append((curr_i, h))
        
        width = len(heights)
        while stack:
            idx, height = stack.pop()
            max_area = max(max_area, (width - idx) * height)

        return max_area




        