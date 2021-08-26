# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def DFS(node, currentMax):
            if(node == None):
                return
            
            if(currentMax <= node.val):
                self.ans += 1
            
            nextMax = max(currentMax, node.val)
            DFS(node.left, nextMax)
            DFS(node.right, nextMax)
        
        DFS(root, -float("inf"))
        return self.ans