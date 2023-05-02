# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    length = 0
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.length
        
        def dfs(node):
            if not node:
                return 0
            
            len_left= dfs(node.left)
            len_right = dfs(node.right)
            
            
            if node.left and node.left.val == node.val:
                len_left = len_left + 1
            else:
                len_left = 0
            if node.right and node.right.val == node.val:
                len_right = len_right + 1
            else:
                len_right = 0
            
                
            self.length = max(len_left+len_right, self.length)
            
            return max(len_left, len_right)
        
        dfs(root)
        
        return self.length