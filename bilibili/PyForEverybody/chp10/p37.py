# like deconstruct in javascript
(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)

# tuples and dict
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

# tuples are comparable
(0, 1, 2) < (5, 1, 2)
# I guess you can only compare same type of data
(0, 1, 2) < (0, 1, '3')