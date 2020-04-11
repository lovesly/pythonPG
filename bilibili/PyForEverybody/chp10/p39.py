# ex_10
import sys
import os.path as op


fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
fname = '../chp9/' + fname
filePath = op.join(sys.path[0], fname)
han = open(filePath)

di = dict()
for line in han:
  line = line.rstrip()
  wds = line.split()
  for w in wds:
    di[w] = di.get(w, 0) + 1

# print(di)

# x = sorted(di.items())
# print(x[:5])

# vscode intellisense often stops working for no reason, sucks
tmp = list()
for k,v in di.items():
  newt = (v, k)
  tmp.append(newt)
# print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp[:5])

for v,k in tmp[:5]:
  print(k, v)