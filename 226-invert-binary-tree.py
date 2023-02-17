# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(node):
            if node is None:
                return
            left = invert(node.left)
            right = invert(node.right)
            
            # Swap the children
            node.left = right
            node.right = left

            # Returnt the new node
            return node

        # Root will be inverted
        return invert(root)