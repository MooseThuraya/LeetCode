class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # T(logn): on avg its logn where disregard half of a tree at a time, worst n (imbalanced tree)
        # S(1): no call stack used
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                # case where we are at a split
                # case where we are p or q
                return node



        
        #T(n)
        #S(n)
        
        # Approach:
        # We are going to traverse the tree
        # As a node, if both my children return True, then I am the lowestCommonAncestor
        # If one of my children returns true, then that child is the lowestCommonAncestor
        # to help make sense, as a root if one of my children returns True, then the other one has to be a decendent of that True child
        
        def helper(node):
            
            if node is None:
                return None, False
            if node.val == q.val or node.val == p.val:
                return node, True
                
            left, leftRes = helper(node.left)
            right, rightRes = helper(node.right)

            if leftRes and rightRes:
                # both are true, return myself
                return node, True

            elif leftRes and not rightRes:
                # return left
                return left, leftRes

            else:
                # return the right
                return right, rightRes


        node, res = helper(root)

        # Gave an error because the return type was the NODE not the VALUE!
        return node