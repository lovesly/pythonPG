# weird way to init an array
M = [[0] * 10 for i in range(10)]
#print(M)

# not sure if we could import in the middle
import os
inputs = list(map(int, os.read(0, 100).split()))
#print(inputs)

print("Case #%i: %.02f %s" % (12, 42.21, "hello"))