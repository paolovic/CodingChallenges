from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                return True
            
        return False


s = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(s.hasCycle(head))  # True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print(s.hasCycle(head))  # True

head = ListNode(1)
print(s.hasCycle(head))  # False
