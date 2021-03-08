def additive_hash(key, p, m):
    h = initial_value
    for i in range(len(key)):
        h += key[i]
    return h % p % m