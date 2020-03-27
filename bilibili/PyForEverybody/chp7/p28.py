# reading files
import sys
import os.path as op

filePath = op.join(sys.path[0], 'mobx-short.txt')
fh = open(filePath)
print(fh)

for lx in fh:
  ly = lx.rstrip()
  print(ly)
