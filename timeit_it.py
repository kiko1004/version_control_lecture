# importing the required module
import timeit

# code snippet to be executed only once
mysetup = '''
def count_el(lst: list) -> dict:
    d = {}
    for el in lst:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return d
'''

# code snippet whose execution time is to be measured
mycode_v1 = '''
def count_in_t_var_1() -> tuple:
    lst = ['a', 'a', 'c', 'c', 'b']
    outp = ()
    d = count_el(lst)
    for key, value in d.items():
        outp += (key, value)
    return outp
'''

mycode_v2 = '''
def count_in_t_var_2() -> tuple:
    lst = ['a', 'a', 'c', 'c', 'b']
    outp = []
    d = count_el(lst)
    for key, value in d.items():
        outp.append(key)
        outp.append(value)
    return tuple(outp)
'''

# timeit statement
print(timeit.timeit(setup=mysetup,
					stmt=mycode_v1,
					number=1000))
# 8.000000000000021e-05

print(timeit.timeit(setup=mysetup,
					stmt=mycode_v2,
					number=1000))
# 8.83999999999989e-05



