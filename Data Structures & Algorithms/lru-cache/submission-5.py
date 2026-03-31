class Node:
    def __init__(self, key, val, next=None, prev=None ):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    #always want the one at the end 
    #we can use a doubly linked list 
    #use a hashmap for storage that stores both the values 
    #create a node class with

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        #removes a node from the list
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def add(self, node):
        #adds a node to the end of the list
        prev_node, next_node = self.right.prev, self.right
        node.prev, node.next = prev_node, next_node
        prev_node.next = next_node.prev = node

        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #remove it from the cache
            self.remove(self.cache[key])
        node = Node(key,value)
        self.cache[key] = node
        self.add(node)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


        
