class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node
        nei = temp.next.val
        temp.val = nei
        temp.next = temp.next.next
        # T(1)
        # S(1)