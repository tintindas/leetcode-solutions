# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        node = head
        n = 0
        while node:
            n += 1
            node = node.next

        k = k % n

        if not k:
            return head

        scout = head

        for _ in range(k):
            scout = scout.next

        end = head

        while scout.next:
            scout = scout.next
            end = end.next

        new_head = end.next
        end.next = None
        scout.next = head

        return new_head