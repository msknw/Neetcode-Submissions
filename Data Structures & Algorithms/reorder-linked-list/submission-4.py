# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        # 先移动
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next:
            slow = slow.next
            fast = fast.next
        
        # 反转指针
        curr = slow
        dummy = None

        while curr:
            next_node = curr.next
            curr.next = dummy
            dummy = curr
            curr = next_node

        #开始插入
        curr = head
        while fast.next:
            next_forw = curr.next
            next_back = fast.next
            curr.next = fast
            fast.next = next_forw

            curr = next_forw
            fast = next_back
