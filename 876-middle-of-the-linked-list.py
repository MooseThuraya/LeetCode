# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # One Pass Solution
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

        # T(n): n where we go over n/2, which is still n
        # S(1): where we only initialize a fixed number of variables, no scaling with n.


        # Two Pass Solution - Wouldn't work if it has a loop!
        cur = head
        count = 0
        while cur is not None:
            cur = cur.next
            count+=1
        
        target = count//2
        count = 0
        cur = head
        while cur:
            if count == target:
                return cur
            cur = cur.next
            count+=1

        # T(n): n+n where n is the number of nodes in the list
        # S(1): where we only initialize a fixed number of variables, no scaling with n.