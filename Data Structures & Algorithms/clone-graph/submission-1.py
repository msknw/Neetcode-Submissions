"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        q = deque()
        nodemap = {}

        dummy = Node(node.val)
        q.append((dummy, node))

        while q:
            cloned, org = q.popleft()
            if org.neighbors:
                if not cloned.neighbors:
                    cloned.neighbors = []
                for nei in org.neighbors:
                    if nei.val in nodemap:
                        curr = nodemap[nei.val]
                    else:
                        curr = Node(nei.val)
                        nodemap[cloned.val] = cloned
                        q.append((curr, nei))
                    cloned.neighbors.append(curr)
            
        
        return dummy