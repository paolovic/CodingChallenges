from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find mid
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # break linked list
        current = slow.next
        slow.next = None

        # reverse second linked list
        prev = None
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        slow.next = None

        # merge both lists
        h1 = head
        h2 = prev
        while h2 is not None:
            temp = h1.next
            h1.next = h2
            h1 = h1.next
            h2 = temp


sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.reorderList(head)
print(head)  # 1->5->2->4->3


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol.reorderList(head)
print(head)  # 1->4->2->3