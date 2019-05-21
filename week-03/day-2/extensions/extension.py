def add(a, b):
    return a + b

def max_of_three(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

def median(pool):
    if not pool:
        return 
    return pool[int((len(pool) - 1) / 2)]

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    if not hungarian:
        return ''
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
