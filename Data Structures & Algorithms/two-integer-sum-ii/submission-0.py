class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #have a two pointer approach:
        '''
        left starting at 0 and right pointer = len(nums) -  1
        while the left pointer is smaller than right, check if nums[left]
        + nums[right] is equal to the target. If it is, return [left+1, right+1].
        If the sum is greater, shift the right pointer back by one, if sum is lower,
        shift the left pointer to the forward by one. An answer is always guarranted
        '''
        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]
        

        