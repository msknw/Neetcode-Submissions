# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # root not None

        curr = root
        pred = None

        # p 是小的那个
        if p.val > q.val:
            p,q = q,p
        
        # # 蛋疼语句
        # p = p if p.val < q.val else q
        # q = q if q.val > p.val else p

        while curr:
            pred = curr
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                # 左右各有
                break

        if curr.left == p and curr.right == q:
            return curr
        elif curr.left == p and curr == q:
            return curr
        elif curr == p and curr.right == q:
            return curr
        
        return curr