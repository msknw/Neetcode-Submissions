# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # # T:O(m*n), S:O(m+n), 过于条件冗余
        if not root and not subRoot:
            return True
        
        if (root and subRoot) and (root.val == subRoot.val):
            if self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        elif root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False
