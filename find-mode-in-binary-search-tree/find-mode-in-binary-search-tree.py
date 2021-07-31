# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.c = Counter()
        
        def traverse(root):
            if(root == None): return
            
            self.c[root.val] += 1
            
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        res = []
        
        m = max(self.c.values())
        
        for i in self.c:
            if(self.c[i] == m):
                res.append(i)
                
        return res
        