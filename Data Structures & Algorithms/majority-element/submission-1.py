class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        highest, value = None, 0
        for k, v in count.items():
            if v > value:
                highest = k
                value = v
        
        return highest
