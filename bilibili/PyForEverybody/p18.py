# loop
n = 5
while n > 0:
  print(n)
  n = n - 1
print('Blastoff')
print(n)

# break, interesting
while True:
  line = input('> ')
  if line == 'done':
    break
  print(line)
print('Done!')

# continue
while True:
  line = input('>> ')
  if line[0] == '#':
    continue
  elif line == 'done':
    break
  print(line)
print('Done!')