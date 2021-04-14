# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB

        lenA = 0
        while currA:
            lenA += 1
            currA = currA.next

        lenB = 0
        while currB:
            lenB += 1
            currB = currB.next

        if lenA > lenB:
            diff = lenA - lenB
            while diff:
                headA = headA.next
                diff -= 1
        else:
            diff = lenB - lenA
            while diff:
                headB = headB.next
                diff -= 1

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None