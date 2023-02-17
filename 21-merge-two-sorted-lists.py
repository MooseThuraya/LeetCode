class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        dummy = head
        # both are not None
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
            else:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
        
        if list1 and not list2:
            dummy.next = list1
        if list2 and not list1:
            dummy.next = list2
        return head.next