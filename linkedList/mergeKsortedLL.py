"""
First solution is to use kind of merge sort. We will merge lists by pairing them
so first we will have k/2 pairs, then k/4, k/8 etc. So altoghether it will be 
time complexity O(nlogk), n - total elements, k - number of lists.
We need helper function to merge 2 lists and that's all. We iterate as long as
we have more than one list.
"""

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeTwoList(l1, l2))
            
            lists = mergedList
        
        return lists[0]

    def mergeTwoList(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                l1.prev, tail.next = tail, l1
                tail = l1
                l1 = l1.next
            else:
                l2.prev, tail.next = tail, l2
                tail = l2
                l2 = l2.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next

"""
Second solution is to use heap
"""



