import sys
import re
import os.path as op

fname = '../chp8/mobx-short.txt'
filePath = op.join(sys.path[0], fname)
han = open(filePath)

for line in han:
  line = line.rstrip()
  # if re.search('^From:', line):
  if re.search('^X-\S+:', line):
    print(line)