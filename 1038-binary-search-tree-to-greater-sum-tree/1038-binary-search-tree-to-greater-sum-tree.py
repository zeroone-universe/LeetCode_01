# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def LNR(node):
            if not node:
                return
            LNR(node.right)
            self.result += node.val
            node.val = self.result
            LNR(node.left)
            
        LNR(root)
        
        return root