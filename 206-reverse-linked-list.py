# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Recursive Solution

        def helper(cur, prev):
            if cur is None:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return helper(cur, prev)

        return helper(head, None)
        
        # iterative Solution

        # prev = None
        # cur = head
        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
        # return prev