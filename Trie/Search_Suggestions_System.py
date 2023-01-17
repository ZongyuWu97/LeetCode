class Trie:
    def __init__(self):
        self.link = {}
        self.suggestion = []
        self.size = 3


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = Trie()
        for product in products:
            self.add(product, root)

        return self.search(root, searchWord)

    def add(self, product, root):
        for ch in product:
            if not ch in root.link:
                root.link[ch] = Trie()
            root = root.link[ch]

            if root.size > 0:
                root.size -= 1
                root.suggestion.append(product)

    def search(self, root, word):
        res = []
        for ch in word:
            if root:
                root = root.link.get(ch)
            res.append(root.suggestion if root else [])

        return res
