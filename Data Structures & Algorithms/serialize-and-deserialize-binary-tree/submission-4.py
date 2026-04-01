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
        # 修正bfs
        queue = deque()
        res = []

        queue.append(root)

        while queue:
            for i in range(len(queue)):
                poped = queue.popleft()
                if poped:
                    res.append(str(poped.val))
                    
                    queue.append(poped.left)
                    queue.append(poped.right)
                else:
                    res.append('#')

        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # 用bfs
        # 最后用','join的所以直接弄就行
        nodes = data.split(',')

        queue = deque()
        if nodes[0] == '#':
            return None
        
        root = TreeNode(nodes[0])
        queue.append(root)

        idx = 1
        while queue:
            poped = queue.popleft()
            if nodes[idx] != '#':
                poped.left = TreeNode(nodes[idx])
                queue.append(poped.left)
            idx += 1

            # 接下来去看right
            if nodes[idx] != '#':
                poped.right = TreeNode(nodes[idx])
                queue.append(poped.right)
            idx += 1
        
        return root
    
        
            







