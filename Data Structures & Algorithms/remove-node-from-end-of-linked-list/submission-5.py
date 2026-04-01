# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # T:O(N), S:O(1)
        # Two pointer, two slow pointer
        # 因为有可能要删头节点，所以要来个dummy
        dummy = ListNode(0, head)
        left = right = dummy

        while n > 0:
            right = right.next
            n -= 1
        
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        
        return dummy.next
