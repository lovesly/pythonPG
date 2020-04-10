import sys
import os.path as op

fname = '../chp9/intro.txt'
filePath = op.join(sys.path[0], fname)

# sorting lists of tuples?
d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
# [('a', 10), ('c', 22), ('b', 1)]
print(sorted(d.items()))

t = sorted(d.items())
for (k, v) in t:
    print(k, v)


# sort by values instead of key
tmp = list()
for k, v in d.items():
    tmp.append((v, k))
print(tmp)

# wow, wtf
tmp = sorted(tmp, reverse=True)
print(tmp)

# top 10 most common words

# reading files
# wowow, life is short, use python!
han = open(filePath)
counts = dict()
for line in han:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for (v, k) in lst[:10]:
    print(k, v)


# wtf
short = sorted([(v, k) for k, v in counts.items()], reverse=True)
for (v, k) in short[:10]:
    print(k, v)
