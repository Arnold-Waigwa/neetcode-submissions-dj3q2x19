"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None}
        curr = head

        while curr:
            node = Node(curr.val)
            hashmap[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            node = hashmap[curr]
            node.next = hashmap[curr.next]
            node.random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]
