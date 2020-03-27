xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
# seems like python also has some kind of precision issue like javascript?
xp = float(xh) * float(xr)
print("Pay", xp)