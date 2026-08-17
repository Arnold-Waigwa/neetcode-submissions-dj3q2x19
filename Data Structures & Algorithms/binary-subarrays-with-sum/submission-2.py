class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(target):
            if target < 0:
                return 0
            l = 0
            total = 0
            res = 0

            for r in range(len(nums)):
                total += nums[r]

                while total > target:
                    total -= nums[l]
                    l += 1

                res += (r - l + 1)
            
            return res
        
        return atMost(goal) - atMost(goal - 1)
