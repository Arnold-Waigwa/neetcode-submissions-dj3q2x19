# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if you have two pointer, if the faster one eventually
        #overlaps the slower one, there exists a cycle
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next
        return False

        