# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #two ways to do this: hashset and slow and tortoise and hair
        #algortithm
        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
            

        