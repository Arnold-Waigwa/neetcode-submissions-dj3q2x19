class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap or set
        return len(nums) != len(set(nums))

