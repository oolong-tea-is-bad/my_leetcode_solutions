# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        header = ListNode()
        trailer = header
        
        while l1 and l2:
            trailer.next = ListNode(l1.val + l2.val)
            if l1.val + l2.val >= 10:
                trailer.next.val -= 10
                if not l1.next and not l2.next:
                    trailer.next.next = ListNode(1)
                elif not l1.next:
                    l2.next.val += 1
                elif not l2.next:
                    l1.next.val += 1
                else:
                    l1.next.val += 1
            l1 = l1.next
            l2 = l2.next
            trailer = trailer.next
                    
        if l1:
            while l1:
                trailer.next = ListNode(l1.val)
                if l1.val == 10:
                    trailer.next.val = 0
                    if l1.next:
                        l1.next.val += 1
                    else:
                        trailer.next.next = ListNode(1)
                l1 = l1.next
                trailer = trailer.next
        
        elif l2:
            while l2:
                trailer.next = ListNode(l2.val)
                if l2.val == 10:
                    trailer.next.val = 0
                    if l2.next:
                        l2.next.val += 1
                    else:
                        trailer.next.next = ListNode(1)
                l2 = l2.next
                trailer = trailer.next
                
        return header.next