from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s.reverseList(head)
print(head.val)  # 5
print(head.next.val)  # 4
print(head.next.next.val)  # 3  
print(head.next.next.next.val)  # 2
print(head.next.next.next.next.val)  # 1

head = ListNode(1, ListNode(2))
s.reverseList(head)
print(head.val)  # 2
print(head.next.val)  # 1

head = ListNode(1)
s.reverseList(head)
print(head.val)  # 1

head = None
s.reverseList(head)
print(head)  # None
