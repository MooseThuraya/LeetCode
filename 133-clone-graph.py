"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visitedHash = {}
        def cloner(node):
            if visitedHash.get(node.val) is not None:
                return visitedHash[node.val]
            
            clone = Node(node.val)
            visitedHash[node.val] = clone

            for nei in node.neighbors:
                clone.neighbors.append(cloner(nei))
            return clone

        if node is None:
            return None
        
        clonedNode = cloner(node)
        return clonedNode
# T(n) where n is the number of nodes on the cloneGraph
# S(n) where we are storing n nodes in the map