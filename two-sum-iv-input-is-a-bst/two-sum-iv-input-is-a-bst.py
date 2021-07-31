# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.l = []
        
        def traverse(root):
            if(root == None):
                return
            
            traverse(root.left)
            self.l.append(root.val)
            traverse(root.right)
            
        traverse(root)
        
        c = {}
        for i in self.l:
            if(i in c):
                c[i] += 1
            else:
                c[i] = 1
        
        for i in self.l:
            c[i] -= 1
            
            rem = k-i
            if(rem in c and c[rem] > 0):
                return True
        
        return False
            