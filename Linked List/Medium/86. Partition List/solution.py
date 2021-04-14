# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        pre_head = ListNode()
        post_head = ListNode()

        pre_curr = pre_head
        post_curr = post_head

        curr = head

        while curr:
            if curr.val < x:
                pre_curr.next = curr
                pre_curr = pre_curr.next
            else:
                post_curr.next = curr
                post_curr = post_curr.next
            curr = curr.next

        post_curr.next = None
        pre_curr.next = post_head.next

        return pre_head.next