# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanced(node):
            if node is None:
                return 0, True
            
            leftHeight, leftRes = balanced(node.left)
            rightHeight, rightRes = balanced(node.right)

            curHeight = max(leftHeight, rightHeight)

            if abs(leftHeight-rightHeight) > 1:
                return curHeight + 1, False
            elif leftRes == False or rightRes == False:
                return curHeight + 1, False
            else:
                # we are still balanced
                return curHeight + 1, True 

        
        _, res = balanced(root)
        return res