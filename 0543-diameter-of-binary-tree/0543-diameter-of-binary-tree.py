# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_dia = 0
        
        def max_length(node):
            if node.left:
                left_length = max_length(node.left)
            else:
                left_length = -1
                
            if node.right:
                right_length = max_length(node.right)
            else:
                right_length = -1
                
            self.max_dia = max(self.max_dia, left_length + right_length +2)
            
            return max(1+left_length, 1+right_length)
        
        max_length(root)
        
        return self.max_dia
            
            
        
  