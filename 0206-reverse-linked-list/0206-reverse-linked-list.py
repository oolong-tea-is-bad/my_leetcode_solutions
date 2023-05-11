# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headDic = {}
        index = 0
        
        # 딕셔너리에 index+1을 key, 그 node의 값을 value
        while head:
            index += 1
            
            headDic[index] = head.val
            head = head.next
            
        # 일반적인 linked list 만드는 과정
        header = ListNode(None)
        starter = header
        
        for i in range(index, 0, -1):
            starter.next = ListNode(headDic[i])
            starter = starter.next
        
        return header.next
            