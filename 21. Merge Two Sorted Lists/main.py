from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        p0 = dummy

        while list1 and list2:
            if list1.val > list2.val:
                p0.next = list2
                list2 = list2.next
            else:
                p0.next = list1
                list1 = list1.next
            p0 = p0.next
        
        if list1 is not None:
            p0.next = list1
        else:
            p0.next = list2

        return dummy.next


s = Solution()
head = ListNode(1, ListNode(2, ListNode(4)))
head2 = ListNode(1, ListNode(3, ListNode(4)))
s.mergeTwoLists(head, head2)  # 1->1->2->3->4->4
print(head.val)  # 1

head = ListNode()
head2 = ListNode()
s.mergeTwoLists(head, head2)  # []
print(head)  # None

head = ListNode()
head2 = ListNode(0)
s.mergeTwoLists(head, head2)  # 0
print(head.val)  # 0
