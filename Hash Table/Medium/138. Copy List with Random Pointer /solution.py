# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None
        node = head
        d = {}

        while node:
            new_node = Node(node.val)
            d[node] = new_node
            node = node.next

        node = head
        new_head = d[head]

        while node:
            new_node = d[node]
            if node.next:
                new_node.next = d[node.next]
            if node.random:
                new_node.random = d[node.random]
            node = node.next

        return new_head
