# unicode
# the ord function tells us the numeric value
print(ord('H'))
print(ord('e'))
print(ord('\n'))

x = u'Hello'
print(type(x))

x = b'abc'
print(type(x))

# strings to bytes, need to decode
# question, what is the type of decode function???
x = b'10'
print(x.decode())

y = '10'
print(y.encode())
print(y.encode().decode())

# how to use ord()'s return value?? transfer the char code to real characters????