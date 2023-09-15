from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        p0 = dummy

        k = len(lists)
        p = []
        for i in range(k):
            p.append(lists[i])
            



s = Solution()
head = ListNode(1, ListNode(4, ListNode(5)))
head2 = ListNode(1, ListNode(3, ListNode(4)))
head3 = ListNode(2, ListNode(6))
s.mergeKLists([head, head2, head3])  # 1->1->2->3->4->4->5->6

head = ListNode()
s.mergeKLists([head])  # []
print(head)  # None

head = ListNode()
head2 = ListNode(0)
s.mergeKLists([head, head2])  # 0

