# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #use mod for reminder
        #use // for carry
        #initialize a dummy node and two pointer and curry
        dummy = pointer = ListNode()
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            value = carry + l1_val + l2_val
            node_val = value % 10
            carry = value // 10
            node = ListNode(node_val)
            pointer.next = node
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

