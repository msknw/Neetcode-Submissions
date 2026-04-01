# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 要搞清楚就是head到底是什么，然后就是什么类型，有什么样的方法
        # T:O(n), S:O(n)
        # 用递归，感觉还挺有意思的
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None

        return new_head
        
