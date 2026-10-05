class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            temp = first
            first = max(
                nums[i] + second,
                first
            )
            second = temp

        return first

        