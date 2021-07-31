# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        
        def descend(root):
            if(root == None):
                return 0
            
            f = descend(root.left)
            s = descend(root.right)
            
            
            self.res = max(self.res, f+s)
            
            return max(f,s)+1
        
        descend(root)
        return self.res