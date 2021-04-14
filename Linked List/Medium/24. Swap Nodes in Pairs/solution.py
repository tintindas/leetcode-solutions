# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = None
        first = head
        second = head.next
        next_pair = None

        while first and second:
            next_pair = second.next

            if prev:
                prev.next = second
            else:
                head = second

            second.next = first
            first.next = next_pair

            prev = first

            first = next_pair

            if not first:
                break
            second = first.next

        return head
