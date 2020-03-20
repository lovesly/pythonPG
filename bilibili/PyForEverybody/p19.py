for i in [5, 4, 3, 2, 1]:
  print(i)
print('Blastoff')

largest = -1
print('Before', largest)

for num in [9, 41, 13, 3, 84, 15]:
  if num > largest:
    largest = num
  print(largest, num)
print('After', largest)

# is operator
# None
# is not
smallest = None
print('Before')
for val in [9, 41, 12, 3, 84, 15]:
  if smallest is None:
    smallest = val
  elif val < smallest:
    smallest = val
  print(smallest, val)
print('After', smallest)