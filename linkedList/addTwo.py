from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        prev = dummy_head
        carry = 0
        curr_l1 = l1
        curr_l2 = l2

        while curr_l1 or curr_l2 or carry:
            if curr_l1 and curr_l2:
                new_val = curr_l1.val + curr_l2.val + carry
                curr_l1 = curr_l1.next
                curr_l2 = curr_l2.next
            elif curr_l1:
                new_val = curr_l1.val + carry
                curr_l1 = curr_l1.next
            elif curr_l2:
                new_val = curr_l2.val + carry
                curr_l2 = curr_l2.next
            else:
                new_val = carry
            
            new_node = ListNode(new_val % 10)
            carry = new_val // 10
            prev.next = new_node
            prev = prev.next

        return dummy_head.next
