def sfsfsdgf(words, n):
    res = 0
    for word in words:
        res += answer(word, n)
    return res

def answer(word, n):
    prev = ''
    count = 0
    for ch in word:
        if ch == prev:
            count += 1
        else:
            if count == n:
                return True
            count = 1
        prev = ch
    return True if count == n else False
    

print(sfsfsdgf(['abc', 'abaaaccct', 'abaaaa', 'aaaaba'], 3))
