class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        #check if the target is in the correct row
        top, bottom = 0, rows-1
        while top <= bottom:
            midrow = (top + bottom) // 2
            if target < matrix[midrow][0]:
                bottom = midrow - 1
            elif target > matrix[midrow][-1]:
                top = midrow + 1
            else:
                break
        
        if top > bottom:
            return False
        else:
            row = (top + bottom) // 2
            l,r = 0, cols - 1
            while l <= r:
                mid = (l + r) // 2
                if target < matrix[row][mid]:
                    r = mid - 1
                elif target > matrix[row][mid]:
                    l = mid + 1
                else:
                    return True
        return False
        
      

