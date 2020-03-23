# string part1
fruit = 'banana'
for letter in fruit:
  print(letter)

# equivalent
index = 0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1

# slicing strings
s = 'Mighty mango'
# up to but not including end
print(s[0:4])
print(s[:2])
print(s[:])
print('n' in s)

# string library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(type(greet))

# searching a string
pos = greet.find('B')
print(pos)

nstr = greet.replace('Bob', 'Jane')
print(nstr)

# strip, or trim
greet = '  Hello Bob '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())
print(greet.startswith('H'))
print(greet.endswith(' '))

# find
data = 'From stephen.marquard@uct.ac.za Sat Jan 5'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# in python3 all strings are unicode
x = u'干'
print(type(x))