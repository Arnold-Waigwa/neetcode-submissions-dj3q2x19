# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #have a dummy node
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        #now we are at the correct point with slow before the target
        #severe links by pointing slow to slow.next.next
        slow.next = slow.next.next
        return dummy.next
