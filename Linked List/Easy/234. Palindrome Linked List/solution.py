# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverse(head: ListNode) -> ListNode:
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

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return None

        slow = fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        head2 = self.reverse(slow)

        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True