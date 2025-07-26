from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            kth_node = self.find_kth_node(prev_group, k)
            if not kth_node:
                break

            next_group = kth_node.next
            
            prev, curr = kth_node.next, prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp_start = prev_group.next
            prev_group.next = kth_node
            temp_start.next = next_group

            prev_group = temp_start
        
        return dummy.next
    
    def find_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
