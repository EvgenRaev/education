


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 15, 'b': 10, 'd': 17}

def dict_mul(d1, d2):
    d3 = dict()
    for k in d1:
        if k in d2:
            d3[k] = d1[k] * d2[k]
    return d3

print (dict_mul(dict1, dict2))

