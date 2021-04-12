# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        carry = 0
        prev = head

        while l1 or l2:

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            res = num1 + num2 + carry

            node = ListNode(res % 10)
            carry = res // 10

            prev.next = node
            prev = prev.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            node = ListNode(carry)
            prev.next = node

        return head.next