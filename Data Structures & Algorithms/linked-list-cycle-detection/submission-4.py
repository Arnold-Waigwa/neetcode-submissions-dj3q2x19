# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #we can use hashmap or do it in place
        #we can use hare and tortoise approach
        #have the hare go until it catches up with the tortoise
        hare, tortoise = head, head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True
        return False

        