# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return []

            return (inorder(root.left) + [root.val] + inorder(root.right))
        
        tlst = inorder(root)

        for i in range(len(tlst)-1):
            if tlst[i+1] <= tlst[i]:
                return False
        return True

        
    