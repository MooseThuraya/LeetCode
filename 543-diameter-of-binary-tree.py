# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDiameter = 0

        def diameterHelper(node):

            if node is None:
                return 0

            left = diameterHelper(node.left)
            right = diameterHelper(node.right)

            currentDiameter = left + right
            self.maxDiameter = max(self.maxDiameter, currentDiameter)

            return max(left, right) + 1

        diameterHelper(root)

        return self.maxDiameter

        # T(n) where n is the number of nodes in the tree
        # S(n) is the hight of the tree. At a worst case, all nodes are skewed to one side, making it O(n) 