class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 1. Extract values into a standard Python list
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        # 2. Sort the nodes by their value using Timsort (O(n log n))
        nodes.sort(key=lambda x: x.val)
        
        # 3. Re-link the nodes to reconstruct the linked list
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None # Terminate the list
        
        return nodes[0]
