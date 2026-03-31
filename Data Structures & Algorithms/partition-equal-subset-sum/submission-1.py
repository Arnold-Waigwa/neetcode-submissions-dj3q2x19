class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums) % 2) != 0:
            return False
        target = sum(nums) // 2
        memo = set()
        memo.add(0)
        for num in nums:
            new_nums = set()
            for s in memo:
                new_num = s + num
                if new_num == target: return True
                new_nums.add(new_num)
            memo.update(new_nums)
        return target in memo


            

