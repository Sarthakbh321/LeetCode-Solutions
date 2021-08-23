# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def traverse(root):
            if(root == None):
                return
            
            if(root.val == target.val):
                return root
            
            return traverse(root.left) or traverse(root.right)
        
        return traverse(cloned)
        