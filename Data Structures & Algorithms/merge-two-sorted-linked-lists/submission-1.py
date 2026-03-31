# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Dummy node to simplify the merging process
        tail = dummy  # Pointer to the end of the merged list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Add list1's node if it has a smaller value
                list1 = list1.next  # Move list1 to the next node
            else:
                tail.next = list2  # Add list2's node if it has a smaller or equal value
                list2 = list2.next  # Move list2 to the next node
            tail = tail.next  # Move the tail pointer forward

        # Add any remaining nodes from either list1 or list2
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next  # Return the merged list, starting from the first real node
