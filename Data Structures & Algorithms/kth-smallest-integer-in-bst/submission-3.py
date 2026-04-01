# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # T:O(n) S:O(n)
        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        lst = inorder(root)
        return lst[k-1]