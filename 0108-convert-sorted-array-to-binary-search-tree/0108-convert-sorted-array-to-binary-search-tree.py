# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# NeetCode Solution: https://www.youtube.com/watch?v=0K0uCMYq5ng&t=517s&ab_channel=NeetCode

class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(l, r):
            # Base case where either the left or right subtrees
            # is iterated completely 
            if l > r:
                return None
            
            # Midpoint
            m = (l+r) // 2
            
            # Root node defined
            root = TreeNode(nums[m])
            # Root's subtrees are made through the recursion
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            
            return root
            
        return helper(0, len(nums)-1)