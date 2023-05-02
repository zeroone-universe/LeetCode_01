# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(node):
            if not node:
                return True, 0

            tf_left, dep_left = dfs(node.left)
            tf_right,dep_right = dfs(node.right)
            if abs(dep_left-dep_right) <=1:
                tf_cur = True
            else:
                tf_cur = False
                
            tf = tf_left & tf_right & tf_cur
            
            dep = max(dep_left,dep_right) + 1
            return tf, dep
        
        tf_root, dep_root = dfs(root)
            
        return tf_root