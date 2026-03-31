class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product_min, product_max = 1, 1
        res = max(nums)

        for i in range(len(nums)):
            temp = product_max
            product_max = max(product_max * nums[i], product_min * nums[i], nums[i])
            product_min = min(temp * nums[i], product_min * nums[i], nums[i])
            res = max(res, product_max)
        return res