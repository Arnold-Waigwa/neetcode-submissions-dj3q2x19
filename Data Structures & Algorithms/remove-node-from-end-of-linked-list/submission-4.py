# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #have a dummy pointing to the head
        #loop until you reach n
        #start two pointers 
        dummy = ListNode(0, head)
        left = right = dummy
        while n:
            right = right.next
            n -= 1
        
        while right.next:
            right = right.next
            left = left.next

        #left right before the node to be removed
        left.next = left.next.next
        return dummy.next


        