# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # T:O(n), S:O(1)
        # optimal：优化一下这个一些细节：
        # 1. 中点的寻找 2. 链表断开 3.兼容奇偶长度链表
        slow = head
        # 通过往这个fast移动提前移一个来对循环的调整让slow刚好到中点
        # 通过移动不同的fast次数感觉可以达到很多有意思的事情的感觉
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # == 反转后面的链表
        second = slow.next
        slow.next = prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # prev 刚好在最后
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            second.next = tmp1
            first.next = second

            first = tmp1
            second = tmp2


            
