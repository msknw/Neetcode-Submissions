# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = list1
        nhead = list2

        dummy = ListNode()
        curr = dummy
        while curr:
            print(curr.val)
            if head and nhead:
                if head.val < nhead.val:
                    next_node = head
                    head = head.next
                else:
                    next_node = nhead
                    nhead = nhead.next
            elif head:
                next_node = head
                head = head.next
            elif nhead:
                next_node = nhead
                nhead = nhead.next
            else:
                next_node = None
            
            curr.next = next_node
            curr = curr.next
        
        return dummy.next