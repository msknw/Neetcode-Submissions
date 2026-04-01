# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # T:O(N), S:O(1)
        # 但毛病很多，比如要pass两次
        ct = 0
        curr = head
        while curr:
            ct += 1
            curr = curr.next
        
        length = ct
        ct = 0

        prev = None
        curr = head
        target = length - n 
        while curr:
            if ct == target:
                if prev != None:
                    prev.next = curr.next
                    curr.next = None
                    break
                else:
                    head = curr.next
                    curr.next = None
                    break
            prev = curr
            curr = curr.next
            ct += 1
        
        return head
