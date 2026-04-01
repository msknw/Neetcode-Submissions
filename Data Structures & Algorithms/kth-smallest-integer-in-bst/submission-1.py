# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 其实也可以不用全部做完就是一步步迭代，如果够了可以就停止了
        stack = []
        curr = root
        cnt = 0

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                poped = stack.pop()
                cnt += 1
                if cnt == k:
                    return poped.val
                
                curr = poped.right