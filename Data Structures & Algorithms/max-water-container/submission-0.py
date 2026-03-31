class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        -two pointer approach
        -variable that stores the largest area
        -we start at the left, and right. Then calculate the area and compare
        if it is bigger then save the bigger area. Shift the pointer of the smaller to the next one, since
        the largest area can only the one with the bigger height.
       -Loop on until the left and right pointer intersect"""
        largest_area = 0
        left, right = 0, len(heights) - 1
        while left < right:
            #area = h * w = height lower = min(height[l], height[r])
            height = min(heights[left], heights[right])
            width = (right - left) 
            area = height * width
            largest_area = max(largest_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return largest_area
        