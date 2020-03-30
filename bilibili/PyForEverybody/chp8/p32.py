# reading files
import sys
import os.path as op

filePath = op.join(sys.path[0], 'mobx-short.txt')
han = open(filePath)

# 1
# for line in han:
#   line = line.rstrip()
#   wds = line.split()
#   # python 难道没有逻辑机制吗？
#   # and 和 & 区别呢？
#   if (len(wds) > 0) and (wds[0] != 'From'):
#     continue
#   if len(wds) > 2: print(wds[2])

# 2
for line in han:
  line = line.rstrip()
  wds = line.split()
  # python 难道没有逻辑机制吗？
  # and 和 & 区别呢？
  if (len(wds) < 1):
    continue
  if wds[0] != 'From': 
    continue
  if len(wds) > 2: 
    print(wds[2])