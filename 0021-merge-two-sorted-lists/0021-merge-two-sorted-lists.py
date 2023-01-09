# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        header = ListNode()
        trailer = header

        while list1 and list2:
            if list1.val > list2.val:
                trailer.next = list2
                list2 = list2.next
            else:
                trailer.next = list1
                list1 = list1.next

            trailer = trailer.next

        if list1:
            trailer.next = list1
        elif list2:
            trailer.next = list2

        return header.next