import sys
import re
import os.path as op

fname = '../chp8/mobx-short.txt'
filePath = op.join(sys.path[0], fname)
han = open(filePath)
numlist = list()

for line in han:
  line = line.rstrip()
  # wtf is [0-9.], 匹配 . 难道不需要斜杠转义吗，可能是在中括号中，默认是符号？
  stuff = re.findall('^X-DSPAM-Confidence: ([0-9\.]+)', line)
  if len(stuff) != 1: continue
  num = float(stuff[0])
  numlist.append(num)
print('Maximum: ', max(numlist))