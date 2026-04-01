# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)

        while queue:
            tmplst = []
            for i in range(len(queue)):
                poped = queue.popleft()
                if poped.left:
                    queue.append(poped.left)
                if poped.right:
                    queue.append(poped.right)
                tmplst.append(poped.val)
            res.append(tmplst)
        
        return res
