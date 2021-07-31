# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        
        def traverse(root):
            if(root == None):
                return 0
            
            f = traverse(root.left)
            s = traverse(root.right)
            
            self.res = self.res and (abs(f-s) <= 1)
            
            return max(f,s)+1
        
        traverse(root)
        return self.res
            
            