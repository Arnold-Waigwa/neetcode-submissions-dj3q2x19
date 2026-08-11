class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[mid][-1]:
                left = mid + 1

            elif target < matrix[mid][0]:
                right = mid - 1

            else:
                nums = matrix[mid]
                l, r = 0, len(nums) - 1

                while l <= r:
                    m = (l + r) // 2

                    if target > nums[m]:
                        l = m + 1
                    elif target < nums[m]:
                        r = m - 1
                    else:
                        return True

                return False

        return False