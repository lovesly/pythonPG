# reading files
import sys
import os.path as op

fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'

filePath = op.join(sys.path[0], fname)
han = open(filePath)

di = dict()
for line in han:
  line = line.rstrip()
  # print(line)
  wds = line.split()
  for w in wds:
    # version 1
    # if w in di:
    #   di[w] = di[w] + 1
    #   print('**EXISTING**')
    # else:
    #   di[w] = 1
    #   print('**NEW**')

    # version 2
    # oldcount = di.get(w, 0)
    # print(w, 'old', oldcount)
    # newcount = oldcount + 1
    # di[w] = newcount
    # print(w, 'new', newcount)

    # idiom: retrive/create
    di[w] = di.get(w, 0) + 1
    # print(w, 'new', di[w])

# print(di)

max = -1
res = None
for k, v in di.items():
  if v > max:
    max = v
    res = k
print('Done: ', res, max)