# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0

        def traverse(node, max):
            if node is None:
                return
            if node.val >= max:
                self.goodCount+=1
                max = node.val
            
            traverse(node.left, max)
            traverse(node.right, max)

        traverse(root, float("-inf"))

        return self.goodCount

        # T(n): go thru all the nodes in the tree
        # S(n): the call stack would be the height of the tree n