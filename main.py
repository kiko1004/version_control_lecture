def count_el(lst: list) -> dict:
    d = {}
    for el in lst:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return d

# In: ['a', 'a', 'c', 'c', 'b']
# Out: (a, 2, c, 2, b, 1)

def count_in_t(lst: list) -> tuple:
    outp = ()
    # outp = []
    d = count_el(lst)
    for key, value in d.items():
        outp += (key, value)
        # outp.append(key)
        # outp.append(value)
    return tuple(outp)

print(
    count_in_t(['a', 'a', 'c', 'c', 'b'])
)

# Timeit test has been done!