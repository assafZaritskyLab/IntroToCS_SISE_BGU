## Unpacking

counts = {'apples': 2, 'oranges': 1}
x, y = counts
print(x)
print(y)

counts = {'apples': 2, 'oranges': 1}
dict_iter = iter(counts)
print(next(dict_iter))
print(next(dict_iter))

