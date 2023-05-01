# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        max_depth = [0]
        
        def dfs(v, k):
            max_depth[0] = max(max_depth[0], k)
            
            if v.left:
                dfs(v.left, k+1)
            if v.right:
                dfs(v.right, k+1)
                
        dfs(root, 1)
        
        return max(max_depth)