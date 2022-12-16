class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def isPrice(word):
            n = len(word)
            if not word[0] == '$' or n == 1:
                return False
            for i in range(1, n):
                if not word[i].isdigit():
                    return False
            return True

        def applyDiscount(word):
            num = int(word[1:])
            return '$%.2f' % (num * (100 - discount) / 100)

        sentences = sentence.split(' ')
        for i in range(len(sentences)):
            if isPrice(sentences[i]):
                sentences[i] = applyDiscount(sentences[i])
        return ' '.join(sentences)
