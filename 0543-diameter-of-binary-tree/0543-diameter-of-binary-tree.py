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
        max_dia = [0]
        
        def max_length(node):
            if node.left:
                left_length = max_length(node.left)
            else:
                left_length = -1
                
            if node.right:
                right_length = max_length(node.right)
            else:
                right_length = -1
                
            max_dia[0] = max(max_dia[0], left_length + right_length +2)
            
            return max(1+left_length, 1+right_length)
        
        max_length(root)
        
        return max_dia[0]
            
            
        
  