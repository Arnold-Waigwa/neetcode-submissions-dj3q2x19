# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        use a helper function to continously merge two lists together
        while lists > 1, merge the two fist list together
        keep until list is one then return the list
        """
        def merge(l1, l2):
            dummy = curr = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(merge(list1,list2))
            lists = merged_lists
        return lists[0]


        