# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # at least one node
        # assume all keys are unique
        # traverse the tree
        # if i go right, update the max
        # if i go left, update the minimum

        def dfs(node, min, max):
            if node is None:
                return True
            if not(node.val < max and node.val > min):
                return False

            leftRes = dfs(node.left, min, node.val)
            rightRes = dfs(node.right, node.val, max)

            if not (leftRes and rightRes):
                # one or more is false
                return False
            else:
                # both are true
                return True

        return dfs(root, float('-inf'),float('inf'))

        # T(n) where n is the number of nodes in the tree
        # S(n) where n is the height of the tree and all nodes are on one side