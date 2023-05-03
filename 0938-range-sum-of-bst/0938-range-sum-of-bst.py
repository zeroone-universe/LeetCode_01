# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    output = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def rangeSum(node):
            if not node:
                return
            elif low <= node.val <= high:
                self.output+=node.val
                rangeSum(node.left)
                rangeSum(node.right)
            elif node.val < low:
                rangeSum(node.right)
            elif node.val > high:
                rangeSum(node.left)
                
        rangeSum(root)
        return self.output