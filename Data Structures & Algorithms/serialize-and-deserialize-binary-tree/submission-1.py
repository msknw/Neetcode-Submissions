# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # 用dfs
        def dfs(root):
            if not root:
                return ',#'
            
            return (',' + str(root.val) + dfs(root.left) + dfs(root.right))
        
        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # 用preorder弄
        nodes = data.split(',')[1:]
        print(nodes)
        idx = 0

        def dfs():
            nonlocal idx

            if nodes[idx] == '#':
                idx += 1
                return None
            
            root = TreeNode(nodes[idx])
            idx += 1

            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()
    
        
            







