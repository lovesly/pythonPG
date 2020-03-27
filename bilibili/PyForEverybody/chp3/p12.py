x = 10
if x < 2 :
  print('small')
elif x < 10 :
  print('medium')
else :
  print('large')
print('All done')

# try catch
astr = "Hello Bob"
try:
  istr = int(astr)
except:
  istr = -1
print('First', istr)

astr = '123'
try:
  istr = int(astr)
except:
  istr = -1
print('Second', istr)
