# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = head
        curr = head.next

        while curr:
            if curr.val != prev.val:
                prev.next = curr
                prev = prev.next

            curr = curr.next

        prev.next = None

        return head
