# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #have two pointers and make the first one go ahead until 
        dummy = second = ListNode(0, head)
        first = head
        k = n
        while k and first:
            first = first.next
            k -= 1
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next

