some_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'b', 'i', 'j','n', 'k', 'l', 'm','n']

dublicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(dublicates)