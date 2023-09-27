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
        oldToNew = {None: None} # passes None edge case
        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToNew[cur]
            copy.next = oldToNew[cur.next]
            copy.random = oldToNew[cur.random]
            cur = cur.next
        
        return oldToNew[head]
    # T(n): go thru all nodes twice, two passes n+n=next
    # S(n): maintain a hashmap of n nodes