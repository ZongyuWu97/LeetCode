class LRUCache:
    class Node:
        def __init__(self, key, val) -> None:
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev, node.next = self.head, tmp
        tmp.prev = node
        self.dict[node.key] = node
    
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.dict[node.key]

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        node = self.dict[key]
        res = node.val
        self.addNode(self.Node(node.key, node.val))
        self.deleteNode(node)
        self.dict[key] = self.head.next
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.deleteNode(self.dict[key])
        if len(self.dict) == self.cap:
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key, value))
        self.dict[key] = self.head.next
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)