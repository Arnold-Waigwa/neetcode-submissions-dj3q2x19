class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        check = len(nums) // 2
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > check:
                return num
            
        
