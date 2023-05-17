# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
        
            node = TreeNode(val = preorder[0])
            node_idx_inorder = inorder.index(preorder[0])

            node.left = self.buildTree(preorder[1:node_idx_inorder+1], inorder[:node_idx_inorder])
            node.right =  self.buildTree(preorder[node_idx_inorder+1:], inorder[node_idx_inorder+1:])
        
            return node