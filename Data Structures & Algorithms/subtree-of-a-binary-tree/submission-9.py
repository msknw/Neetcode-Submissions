# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialization(self, root):
        if not root:
            return ',#'

        # 用preorder
        return (',' + str(root.val) + self.serialization(root.left) + self.serialization(root.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 优化一下这个陷阱 + 优化一下root和subRoot空的情况
        # 原来的做法比较花时间，确实感觉直接serialization方便一点
        if not subRoot:
            return True
        if not root:
            return False

        rootstr = self.serialization(root)
        subrootstr = self.serialization(subRoot)

        return subrootstr in rootstr




