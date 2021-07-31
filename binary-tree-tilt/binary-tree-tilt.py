# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.sum = 0
        
        def traverse(root):
            if(root == None):
                return 0
            
            f = traverse(root.left)
            s = traverse(root.right)
            
            diff = abs(f-s)
            self.sum += diff
            
            return root.val + f + s
        
        traverse(root)
        return self.sum