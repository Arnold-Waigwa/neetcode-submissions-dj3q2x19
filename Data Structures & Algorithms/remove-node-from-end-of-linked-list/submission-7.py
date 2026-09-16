# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        second = head
        for _ in range(n):
            second = second.next
        
        first = dummy = ListNode(0, head)

        while second:
            first, second = first.next, second.next
        
        first.next = first.next.next
        return dummy.next
                
