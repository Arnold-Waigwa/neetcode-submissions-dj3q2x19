class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #start a binary search on each row: furtherst right
        #for left pointer and start for right pointer

        l, r = 0, len(matrix)-1

        #start binary search
        while l <= r:
            if matrix[l][-1] < target:
                l += 1

            elif matrix[r][0] > target:
                r -= 1

            else: break

        if not (l <= r): return False
        
        nums = matrix[l]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right) //2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return False