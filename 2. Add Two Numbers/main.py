from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            res.next = ListNode(val=val)
            res = res.next
        return dummy.next


s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(s.addTwoNumbers(l1, l2))  # [7,0,8]

l1 = ListNode(0)
l2 = ListNode(0)
print(s.addTwoNumbers(l1, l2))  # [0]

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
print(s.addTwoNumbers(l1, l2))  # [8,9,9,9,0,0,0,1]
