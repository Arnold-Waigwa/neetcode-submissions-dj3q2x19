class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap or set
        nums_map = {} 
        for num in nums:
             if num in nums_map: return True
             nums_map[num] = 1
        return False

