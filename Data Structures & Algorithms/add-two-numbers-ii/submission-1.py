# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [], []

        while l1:
            num1.append(l1.val)
            l1 = l1.next
        
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        while num1 or num2 or carry:
            val1 = num1.pop() if num1 else 0
            val2 = num2.pop() if num2 else 0

            val3 = val1 + val2 + carry

            rem = val3 % 10
            carry = val3 // 10
            node = ListNode(rem, head)
            head = node
        
        return head

            





        
