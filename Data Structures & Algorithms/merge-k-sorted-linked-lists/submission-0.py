# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #for every head in lists, put it into a list
        #move head to head.next
        array = []
        for li in lists:
            head = li
            while head:
                array.append(head.val)
                head = head.next

        array.sort()
        dummy = curr = ListNode()
        for val in array:
            node = ListNode(val)
            curr.next = node
            curr = curr.next

        return dummy.next
        
