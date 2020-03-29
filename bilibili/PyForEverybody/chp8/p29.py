# list

# range
# 也许是版本问题，和教程中不一致，range 和 list 显然是两种结构
r1 = range(4)
l1 = [0, 1, 2, 3]
print(r1)
for i in range(4):
  print(i)
print(type(r1))
print(type(l1))

# plus === concat
a = [1, 2, 3]
b = [4, 5, 7]
c = a + b
print(c)

# slice
# remember: up to but not including
t = [9, 451, 12, 3, 65, 15]
print(t[1:3])

# 'dir' will list the methods
# print(dir(t))

# build a list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

# in, not in
99 in stuff
20 not in stuff

# Lists are in order
friends = ['J', 'Cln', 'Sally']
friends.sort()

# built-in functions
nums = [3, 41, 12, 98, 73, 14]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
## 精度呢？
print(sum(nums)/len(nums))

# another way to do the same thing

# numlist = list()
# while True:
#   inp = input('Enter a number: ')
#   if inp == 'done': break
#   value = float(inp)
#   numlist.append(value)
# average = sum(numlist)/len(numlist)
# print('Average:', average)

# strings and lists
line = 'why so serious'
arr = line.split()
print(arr)