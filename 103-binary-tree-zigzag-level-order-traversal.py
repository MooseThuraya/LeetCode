# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        res = []
        
        q = collections.deque()
        q.append(root)
        reverse = False
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if reverse:
                level = level[::-1]
            if level:
                res.append(level)
            reverse = not reverse

        return res