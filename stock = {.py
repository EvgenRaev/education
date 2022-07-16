dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 15, 'b': 10, 'd': 17}
dict3 = list
for key, value in dict1.iteritems():
    if key in dict2:
         dict3[key] = int(dict1[key]) * int(dict2[key])

print (dict3)
