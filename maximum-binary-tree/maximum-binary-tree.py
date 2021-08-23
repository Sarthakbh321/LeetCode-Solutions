# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildTree(arr):
            if(len(arr) == 0):
                return None
            
            m = max(arr)
            mInd = -1
            
            for i in range(len(arr)):
                if(arr[i] == m):
                    mInd = i
                    break
            
            root = TreeNode(m)
            root.left = buildTree(arr[:mInd])
            root.right = buildTree(arr[mInd+1:])
            
            return root
        
        return buildTree(nums)