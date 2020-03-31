purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 32
print(purse)

purse['candy'] = purse['candy'] + 3
print(purse)

jjj = { 'chunk': 1, 'fred': 42, 'jan': 100 }
print(jjj)
print(type({}))

# use as a map
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
  if name not in counts:
    counts[name] = 1
  else:
    counts[name] = counts[name] + 1
print(counts)

# get method
name = 'shit'
if name in counts:
  x = counts[name]
else:
  x = 0
print(x)
# equals ...
x = counts.get(name, 0)
print(x)

# so for the above example
# now I understand what 'life is short, use python' means
counts = {}
for name in names:
  counts[name] = counts.get(name, 0) + 1
print(counts)

# loop a dict
for key in counts:
  print(key, counts[key])

# interesting
# remember in js, you can build a set with an array
print(list(counts))
print(counts.keys())
# dict_keys??
print(type(counts.keys()))
print(counts.values())
print(counts.items())
# dict_items 如何从中取值呢
print(type(counts.items()))
# two iteration variables
for aa, bb in counts.items():
  print(aa, bb)

# previous example
print('==============================')
