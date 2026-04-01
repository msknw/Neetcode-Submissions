# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeTwoList(self, head1, head2):
            dummy = ListNode()
            curr = dummy
            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next

            curr.next = head1 or head2

            return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 用分治，分而治之，divide and conquer
        dummy = ListNode()

        if len(lists) == 0:
            return None

        while len(lists) > 1:
            newlsts = []
            n = len(lists)
            for i in range(0, n, 2):
                head1 = lists[i]
                head2 = lists[i+1] if i+1<n else None

                merged = self.mergeTwoList(head1, head2)
                newlsts.append(merged)
            lists = newlsts

        return lists[0]  
        
        

