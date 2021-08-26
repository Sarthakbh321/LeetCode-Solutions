# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = -1*float("inf")
        
        def DFS(node, prevMax, prevMin):
            if(node == None):
                return 
            
            diff1 = abs(node.val-prevMax)
            diff2 = abs(node.val-prevMin)
            
            self.ans = max(self.ans, diff1, diff2)
            
            nextMax = max(node.val, prevMax)
            nextMin = min(node.val, prevMin)
            
            DFS(node.left, nextMax, nextMin)
            DFS(node.right, nextMax, nextMin)
            
        DFS(root, root.val,root.val)
        
        return self.ans
            