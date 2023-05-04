# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}
        while head != None:
            if head.val not in dic:
                dic[head.val] = [head]
            else:
                if head in dic[head.val]:
                    return True
                dic[head.val].append(head)
            
            head = head.next
        
        return False