# python2 doesn't have request method
# import urllib.request, urllib.parse, urllib.error
import urllib
from bs4 import BeautifulSoup

# have to type in 'http://www.dr-chunk.com/page1.htm'
# so fucking weird
url = input('Enter - ')
# read??
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))