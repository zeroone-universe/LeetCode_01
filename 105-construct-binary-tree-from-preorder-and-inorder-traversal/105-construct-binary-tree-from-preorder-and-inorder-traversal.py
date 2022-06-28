# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            n_val = preorder.pop(0)
            node = TreeNode(n_val)
            idx = inorder.index(n_val)
            
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])
        else:
            return None
        return node