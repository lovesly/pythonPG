# reading files
import sys
import os.path as op

# input file name
fname = input('Enter the file name: ')

# wow, join the path
# open file
filePath = op.join(sys.path[0], fname)
try:
  fhand = open(filePath)
except:
  print('File cannot be opened:', fname)
  quit()
# print the file handler
print(fhand)

# ===== read by line =====
count = 0
for cheese in fhand:
  # right strip will get rid of the '\n', interesting
  # since print will produce a '\n', if we don't use strip function, we'll have two newlines
  cheese = cheese.rstrip()
  print(cheese)
  count = count + 1
print('Line count:', count)

# ===== read the whole file =====
fhandle = open(filePath)
inp = fhandle.read()
print(len(inp))
print('100 characters: ============ \n', inp[:100])

# ===== searching =====
# confused, if a file is already read, what's gonna happen?
# seems like the file will be read only once
for line in fhand:
  if (line.startswith('From:')):
    print(line)