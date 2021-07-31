# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        
        def descend(root, dir):
            if(root == None):
                return
            
            if(root.right == None and root.left == None and dir == 0):
                self.sum += root.val
                return
            
            descend(root.left, 0)
            descend(root.right, 1)
            
        descend(root, -1)
        return self.sum