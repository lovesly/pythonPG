def computePay(hours, rate):
  print("In computePay", hours, rate)
  if (hours > 40):
    pay = rate * 40 + rate * 1.5 * (hours - 40)
  else:
    pay = hours * rate
  return pay

xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
try:
  fh = float(xh)
  fr = float(xr)
except:
  print("Error, please enter numeric input")
  quit()

xp = computePay(fh, fr)
print("Pay", xp)