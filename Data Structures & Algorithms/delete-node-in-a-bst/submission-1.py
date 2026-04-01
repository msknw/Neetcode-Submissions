# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root, key):
        # 优化分支
        pred = None
        curr = root

        while curr and curr.val != key:
            pred = curr
            if key > curr.val:
                curr = curr.right
            elif key < curr.val:
                curr = curr.left
        
        # 如果没找到
        if not curr:
            return root

        # 找到了，要删除
        # 下面代码太冗余，改了一改逻辑
        if not curr.right or not curr.left:
            # 返回left
            node = curr.left if not curr.right else curr.right
            
            # 连上
            if not pred:
                # 刚开始的时候，说明删的是根节点
                root = node
            
            else:
                # 建议用指针判断 so 
                if pred.left == curr:
                    pred.left = node
                else:
                    pred.right = node
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


        return root