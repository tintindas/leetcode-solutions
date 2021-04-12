# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head:
            return None

        scout = head
        follow = head

        for _ in range(n):
            scout = scout.next

        if not scout:
            return head.next

        while scout.next:
            scout = scout.next
            follow = follow.next

        temp = follow.next

        follow.next = temp.next

        del temp

        return head