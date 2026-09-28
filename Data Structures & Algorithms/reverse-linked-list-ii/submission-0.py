# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        for _ in range(right):
            prev = prev.next
        
        start = dummy
        for _ in range(left - 1):
            start = start.next

        tail = prev
        curr = dummy
        for _ in range(left):
            curr = curr.next
        
        while curr != tail:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        start.next = prev
        return dummy.next

        




        