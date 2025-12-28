from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_to_copy_map = {}
        if head is None:
            return None
        
        curr = head
        dummy_node = Node(0)
        prev = dummy_node
        curr_copy = dummy_node

        while curr:
            curr_copy = Node(curr.val)
            nodes_to_copy_map[curr] = curr_copy
            prev.next = curr_copy
            prev = curr_copy
            curr = curr.next
        
        # fill random nodes
        copy = dummy_node.next
        org = head

        while org:
            if org.random is None:
                copy.random = None
            else:
                copy.random = nodes_to_copy_map[org.random]
            org = org.next
            copy = copy.next

        return dummy_node.next
