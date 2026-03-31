class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            if matrix[l][-1] < target:
                l += 1
            elif matrix[r][0] > target:
                r -= 1
            else:
                break
        
        if not (l == r):
            return False
        
        array = matrix[l]
        l, r = 0, len(array) - 1
        while l <= r:
            mid = (l+r) // 2
            if array[mid] > target:
                r = mid - 1
            elif array[mid] < target:
                l = mid + 1
            else:
                return True
        return False

        
        