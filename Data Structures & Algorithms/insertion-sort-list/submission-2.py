# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(float("-inf"))
        dummy.next = head
        
        # last_sorted always points to the end of the already sorted part
        # curr is the node we want to insert
        last_sorted = head
        curr = head.next

        while curr:
            if last_sorted.val <= curr.val:
                # Node is already in the correct position, just move forward
                last_sorted = last_sorted.next
            else:
                # Find the correct position to insert curr
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                
                # Remove curr from its current position
                last_sorted.next = curr.next
                
                # Insert curr between prev and prev.next
                curr.next = prev.next
                prev.next = curr
            
            # Move to the next unsorted node
            curr = last_sorted.next
            
        return dummy.next
