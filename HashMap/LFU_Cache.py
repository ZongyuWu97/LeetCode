class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.frequencies = defaultdict(OrderedDict)
        self.cache = {}

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        fre, val = self.cache[key]
        self.insert(key, val, fre + 1)
        self.clear(fre, key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.size <= 0:
            return

        if key in self.cache:
            fre, _ = self.cache[key]
            self.insert(key, value, fre + 1)
            self.clear(fre, key)
            return

        if len(self.cache) == self.size:
            # Pop least frequent element
            keys = self.frequencies[self.minf]
            tmp_key, _ = keys.popitem(last=False)
            del self.cache[tmp_key]

        self.insert(key, value, 1)
        self.minf = 1

    # Add key to cache and frequencies.
    def insert(self, key, val, fre):
        self.cache[key] = (fre, val)
        self.frequencies[fre][key] = val

    # Delete if no key with this frequency.
    def clear(self, fre, key):
        del self.frequencies[fre][key]
        if not self.frequencies[fre]:
            del self.frequencies[fre]
            if self.minf == fre:
                self.minf += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
