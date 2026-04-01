# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

# 重写一下这个ListNode:
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 尝试用堆 heapq
        dummy = ListNode()
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)

        curr = dummy

        while heap:
            min_node = heapq.heappop(heap)
            curr.next = min_node
            curr = min_node
            if min_node.next:
                heapq.heappush(heap, min_node.next)
        
        return dummy.next

