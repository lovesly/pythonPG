# python2 doesn't have request method
# and it seems like we've installed bs4 into python2 env
# to use it in python3, we have to install it again??
# import urllib.request, urllib.parse, urllib.error
import urllib
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# have to type in 'http://www.dr-chunk.com/page1.htm'
url = input('Enter - ')
# read??
html = urllib.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))