# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def DFS(node, target):
            if(node == None):
                return None
            
            leftChild = DFS(node.left, target)
            rightChild = DFS(node.right, target)
            
            node.left = leftChild
            node.right = rightChild
            
            if(leftChild == None and rightChild == None):
                if(node.val == target):
                    return None
                else:
                    return node
            
            return node
        
        
        return DFS(root, target)