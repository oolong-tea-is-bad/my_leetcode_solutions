# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [] 
        stack = []
        cur = root
        
        # ITERATVIE SOLUTION
        while cur or stack:
            # allows cur to keep traversing to cur.left
            while cur:
                stack.append(cur)
                cur = cur.left
            # When cur is None, it brings back the node that is one level above from the stack
            cur = stack.pop()
            res.append(cur.val)
            # Once the left subtree of the cur is complete it goes to the right
            cur = cur.right
            
            # if left and right subtrees are completely done, meaning cur is none, it brings
            # back one of the root nodes that are stored in the stack
        return res
    
    
        # RECURSIVE SOLUTION
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        # inorder(root)
        # return res