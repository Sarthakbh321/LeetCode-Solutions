# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if(not root or (root.left == None and root.right == None)):
                return

            invert(root.left)
            invert(root.right)
            root.left, root.right = root.right, root.left

        invert(root)
        return root