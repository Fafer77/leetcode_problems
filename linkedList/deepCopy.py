from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy_node = Node(head.val)
        org_node = head.next
        copy_head = copy_node
        org_copy_hash = {}
        org_copy_hash[head] = copy_head

        while org_node:
            copy_val = org_node.val
            new_node = Node(copy_val)

            copy_node.next = new_node
            org_copy_hash[org_node] = new_node
            
            copy_node = copy_node.next
            org_node = org_node.next
        
        curr = head
        curr_copy = copy_head
        while curr:
            
            mapped = org_copy_hash[curr.random] if curr.random else None
            curr_copy.random = mapped

            curr = curr.next
            curr_copy = curr_copy.next
        
        return copy_head
        