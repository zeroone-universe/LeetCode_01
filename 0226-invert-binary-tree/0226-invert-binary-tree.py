# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        head = root
        
        def invert(node):
            if node:
                invert(node.left)
                invert(node.right)
            
                if node.left or node.right:
                    node.left, node.right = node.right, node.left
            
        invert(root)
        
        return head