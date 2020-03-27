xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
try:
  fh = float(xh)
  fr = float(xr)
except:
  print("Error, please enter numeric input")
  quit()
if (fh > 40):
  xp = fr * 40 + fr * 1.5 * (fh - 40)
else:
  xp = fh * fr
print("Pay", xp)