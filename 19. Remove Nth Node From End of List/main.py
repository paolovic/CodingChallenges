from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        left = dummy
        right = head
        while right and n > 0:
            right = right.next
            n -= 1
        while right is not None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next


s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s.removeNthFromEnd(head, 2)  # 1->2->3->5
print(head.val)  # 1

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s.removeNthFromEnd(head, 1)  # 1->2->3->4
print(head.val)  # 1

head = ListNode(1)
s.removeNthFromEnd(head, 1)  # []
print(head)  # None

head = ListNode(1, ListNode(2))
s.removeNthFromEnd(head, 2)  # 1
print(head.val)  # 1
