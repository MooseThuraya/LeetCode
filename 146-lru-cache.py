class Node(object):
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}

        # right: most used. left LRU
        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left, self.right
        
    def remove(self, node):
        #TODO
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def insert(self, node):
        #TODO
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # update recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # doesnt exist
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # key exists
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        #after adding, ensure LRU is within capacity
        if len(self.cache) > self.cap:
            # we need to bring it to capicity, rm LRU
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
    
    # T(1): each method is constant on avg
    # S(n): where n is the number of elements in cache == capacity


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)