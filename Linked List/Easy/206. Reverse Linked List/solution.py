# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = None
        curr = head
        nxt = head.next

        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next

        curr.next = prev
        return curr