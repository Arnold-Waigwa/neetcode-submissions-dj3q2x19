# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = []
        for li in lists:
            head = li
            while head:
                output.append(head.val)
                head = head.next

        output.sort()
        dummy = curr = ListNode()
        for val in output:
            node = ListNode(val)
            curr.next = node
            curr = curr.next
        
        return dummy.next

        