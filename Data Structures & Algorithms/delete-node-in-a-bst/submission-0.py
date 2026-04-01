# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left

        return curr

    def deleteNode(self, root, key):
        # iterative ?
        if not root:
            return None
        pred = None
        curr = root
        while curr:
            if key > curr.val:
                pred = curr
                curr = curr.right
            elif key < curr.val:
                pred = curr
                curr = curr.left
            else:
                # 找到了，要删除
                if not curr.right:
                    # 返回left
                    node = curr.left
                    # 连上
                    if not pred:
                        # 刚开始的时候
                        root = node
                    else:
                        if pred.val > curr.val:
                            pred.left = node
                        else:
                            pred.right = node
                    break
                elif not curr.left:
                    node = curr.right
                    # 连上
                    if not pred:
                        # 刚开始的时候
                        root = node
                    else:
                        if pred.val > curr.val:
                            pred.left = node
                        else:
                            pred.right = node
                    break
                else:
                    # 两个都有
                    # 手动找min
                    predSucc = curr
                    succ = curr.right
                    while succ and succ.left:
                        predSucc = succ
                        succ = succ.left
                    
                    # succ 是min
                    curr.val = succ.val

                    # 删掉succ这个，succ只有right child，所以就看这个是在左边还是连右边
                    if succ == predSucc.left:
                        predSucc.left = succ.right
                    else:
                        predSucc.right = succ.right

                    break

        return root