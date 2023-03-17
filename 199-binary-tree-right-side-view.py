import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # len >= 0
        # integers, BT,
        # no nulls
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()

                if node is not None:
                    level.append(node.val)
                    q.append(node.right)
                    q.append(node.left)
            if level:
                res.append(level[0])
        return res