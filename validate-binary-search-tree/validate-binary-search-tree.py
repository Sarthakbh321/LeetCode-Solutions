# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def traverse(root, minPossible, maxPossible):
            if(root == None):
                return True
            
            if(root.val >= maxPossible or root.val <= minPossible):
                return False
            
            return traverse(root.left, minPossible, root.val) and traverse(root.right, root.val, maxPossible)
        
        return traverse(root, -float("inf"), float("inf"))