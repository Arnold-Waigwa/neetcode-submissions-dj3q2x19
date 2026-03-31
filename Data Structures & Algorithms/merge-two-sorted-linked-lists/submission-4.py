# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #start with a dummy node to store the new list
        head = dummy = ListNode()
        l1_pointer, l2_pointer = list1, list2

        while l1_pointer and l2_pointer:
            if l1_pointer.val < l2_pointer.val:
                head.next = l1_pointer
                l1_pointer = l1_pointer.next
            else:
                head.next = l2_pointer
                l2_pointer = l2_pointer.next

            head = head.next
        head.next = l1_pointer or l2_pointer
        return dummy.next


