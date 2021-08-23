# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, depth):
            if(root == None):
                return
                        
            if(traverse.height == depth):
                traverse.sum += root.val
            elif(traverse.height < depth):
                traverse.height = depth
                traverse.sum = root.val
            
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)
            
        
        traverse.sum = 0
        traverse.height = 0
        traverse(root,0)
        
        return traverse.sum