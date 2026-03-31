class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #acknowledge that this is a linked list cycle problem
        #use hare and tortoise to find the meetup point
        #use another loop from head and meetup point;
        #where this two meet, is the duplicate
        
        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
        