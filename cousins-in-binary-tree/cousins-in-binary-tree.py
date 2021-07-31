# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.l1 = -1
        self.l2 = -1
        self.p1 = None
        self.p2 = None
        
        def descend(root, depth, parent):
            if(root == None):
                return
            
            if(root.val == x): 
                self.l1 = depth
                self.p1 = parent
                return
            
            if(root.val == y):
                self.l2 = depth
                self.p2 = parent
                return
            
            descend(root.left, depth+1, root)
            descend(root.right, depth+1, root)
            
        descend(root, 0, None)
        
        if(self.l1 == self.l2 and self.p1 != self.p2):
            return True
        
        return False
                
            