class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash_map.keys():
            node = self.hash_map[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map.keys():
            self.hash_map[key].val = value
            
            node = self.hash_map[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            return
        
        if self.capacity == len(self.hash_map):
            to_delete = self.tail.prev
            self.tail.prev = to_delete.prev
            to_delete.prev.next = self.tail

            del self.hash_map[to_delete.key]

        new_node = ListNode(key, value)
        self.head.next.prev = new_node
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.prev = self.head

        self.hash_map[key] = new_node
