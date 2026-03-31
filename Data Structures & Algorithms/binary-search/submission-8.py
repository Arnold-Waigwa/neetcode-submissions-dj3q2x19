class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def dfs(l, r):
            if l > r:
                return -1
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return dfs(l, mid - 1)
            else:
                return dfs(mid + 1, r)
        return dfs(0, len(nums) - 1)
