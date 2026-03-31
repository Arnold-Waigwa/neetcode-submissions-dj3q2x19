class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if youre the first one in a sequence, keep
        #going until youre not, counting the length in the process
        longest = 0
        numset = set(nums)
        for num in nums:
            if num - 1 not in numset:
                length = 1
                while (num + 1) in numset:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest
        