import re
x = 'My 2 favourite nubmers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

# greedy matching, (* and +) push outward in both directions
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
# non-greedy matching
y = re.findall('^F.+?:', x)
print(y)

#Fine-Tuning string extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)

# parentheses will tell where to start and stop what string to extract
y = re.findall('^From (\S+@\S+)', x)
print(y)