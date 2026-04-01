# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # T:O(n), S:O(n)
        # 不错不错，和答案写的相当一致
        self.result = root.val

        def dfs(root):
            
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            
            leftmax = leftmax if leftmax > 0 else 0
            rightmax = rightmax if rightmax > 0 else 0
            
            uploadval = max(leftmax, rightmax) + root.val
            currval = leftmax + rightmax + root.val

            self.result = max(currval, self.result)

            return uploadval
        
        dfs(root)
        return self.result