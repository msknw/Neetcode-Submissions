# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # T:O(n^2) S:O(n)
        # slice这块就是尽力而为，out of range也是返回空 无所谓
        #先找中值
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        # 肯定在, 这是index
        mid = inorder.index(root.val)

        root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1 : ], inorder[mid+1 :])

        return root