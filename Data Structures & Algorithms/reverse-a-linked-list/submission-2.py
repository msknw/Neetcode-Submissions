# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 要搞清楚就是head到底是什么，然后就是什么类型，有什么样的方法
        # T:O(n), S:O(1)
        # 正常的方法，迭代
        if not head:
            return None

        prev = None
        curr = head
        print(head.val)
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
        
