def fill(collection, value, begin=0, end=None):
    length = len(collection)

    normalized_end = length if end is None or end > length else end

    if begin < 0:
        return collection

    for i in range(begin, normalized_end):
        collection[i] = value

coll = [1, 2, 3, 4]

fill(coll, '*', 0, 10)
print(coll)