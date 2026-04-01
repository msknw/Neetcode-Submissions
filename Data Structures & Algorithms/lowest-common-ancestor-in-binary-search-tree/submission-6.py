# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursive
        # T:O(h), h is height; S:O(h)

        if not root:
            return None
        
        # p is min
        if (root.val > q.val and root.val > p.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (root.val < q.val and root.val < p.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root