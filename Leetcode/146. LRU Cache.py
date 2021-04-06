class Node:
    def __init__(self, key, value, prev=None, nextNode=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = nextNode


class LRUCache:
    # 2:14pm
    def __init__(self, capacity: int):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.node_map = {}  # key -> Node

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # inside nodemap, update location
        # not inside nodemap, pop last and add to front
        if key in self.node_map:
            old_node = self.node_map[key]
            self.remove(old_node)

        node = Node(key, value)
        self.add(node)
        self.node_map[key] = node
        if len(self.node_map) > self.capacity:
            # remove last node
            last_node = self.tail.prev
            self.remove(last_node)
            self.node_map.pop(last_node.key)

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = node.prev = None

    def add(self, new_node):
        first_node = self.head.next
        first_node.prev = new_node
        new_node.next = first_node
        new_node.prev = self.head
        self.head.next = new_node


lRUCache = LRUCache(2)
print(lRUCache.put(1, 1))  # cache is {1=1}
print(lRUCache.put(2, 2))  # cache is {1=1, 2=2}
print(lRUCache.get(1))  # return 1
print(lRUCache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))  # returns -1 (not found)
print(lRUCache.put(4, 4))  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))  # return -1 (not found)
print(lRUCache.get(3))  # return 3
print(lRUCache.get(4))  # return 4
