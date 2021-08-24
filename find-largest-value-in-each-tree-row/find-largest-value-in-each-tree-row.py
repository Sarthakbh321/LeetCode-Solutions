# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution(object):

    def largestValues(self, root):
        
        if(root == None): return []
        
        maxVal = defaultdict(lambda:-float("inf"))

        q = deque([[root, 0]])

        while(len(q) > 0):
            current = q.popleft()
            currentNode = current[0]
            currentDepth = current[1]

            maxVal[currentDepth] = max(maxVal[currentDepth], currentNode.val)

            if(currentNode.left != None):
                q.append([currentNode.left, currentDepth+1])

            if(currentNode.right != None):
                q.append([currentNode.right, currentDepth+1])


        maxDepth = max(maxVal.keys())
        # print(maxDepth)
        res = [None]*(maxDepth+1)

        for i in maxVal:
            # print(i)
            res[i] = maxVal[i]

        return res