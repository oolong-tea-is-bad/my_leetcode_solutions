# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headDic = {}
        index = 0
        
        while head:
            index += 1
            
            headDic[index] = head.val
            head = head.next
            
        header = ListNode(None)
        starter = header
        
        for i in range(index, 0, -1):
            starter.next = ListNode(headDic[i])
            starter = starter.next
        
        return header.next
            