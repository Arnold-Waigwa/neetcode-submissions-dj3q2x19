class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        l, r = 0, len(nums) - 1
        res = 0
        MOD = 10**9 + 7

        powers = [1] * len(nums)
        for i in range(1, len(nums)):
            powers[i] = powers[i - 1] * 2 % MOD

        while l <= r:
            while l <= r and nums[l] + nums[r] > target:
                r -= 1

            if l > r:
                break

            res += powers[r - l]
            res %= MOD
            l += 1

        return res