class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for l in range(len(nums) - 3):
            if l > 0 and nums[l] == nums[l - 1]:
                continue

            for r in range(l + 1, len(nums) - 2):
                if r > l + 1 and nums[r] == nums[r - 1]:
                    continue

                a, b = nums[l], nums[r]

                left, right = r + 1, len(nums) - 1
                while left < right:
                    total = a + b + nums[left] + nums[right]

                    if total > target:
                        right -= 1

                    elif total < target:
                        left += 1
                    
                    else:
                        res.append([a, b, nums[left], nums[right]])

                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        return res

