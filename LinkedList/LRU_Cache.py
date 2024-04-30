class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev, node.next = self.head, tmp
        tmp.prev = node
        self.dict[node.key] = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.dict[node.key]

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        node = self.dict[key]
        res = node.val
        self.removeNode(node)
        self.addNode(Node(node.key, node.val))
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.removeNode(self.dict[key])
        if len(self.dict) == self.capacity:
            self.removeNode(self.tail.prev)

        node = Node(key, value)
        self.addNode(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
