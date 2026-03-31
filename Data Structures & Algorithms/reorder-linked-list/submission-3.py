# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle using hare and tortoise method
        #split the list into half; two identical lists
        #Reverse the second list
        #Merge the two lists 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow behind the midpoint now; split
        second = slow.next
        prev = slow.next = None
        #reverse
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #merge our two heads; second head begins at prev
        first, second = head, prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2




        
        


        

        