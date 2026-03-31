class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #phase 1, let the pointer meet
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #at this point, theyve met
        #start another pointer, which meets slow at duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        