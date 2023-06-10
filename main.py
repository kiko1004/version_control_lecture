def count_el(lst: list) -> dict:
    d = {}
    for el in lst:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return d
