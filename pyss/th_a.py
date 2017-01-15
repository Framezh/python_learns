# -*- coding: utf-8 -*-

## python 2.x
# import urllib
# 
## python 3.x
import urllib.request

url = 'http://www.python.org'
# python 2.x
# html = urllib.

# python 3.x
fp = urllib.request.urlopen(url)
mybyte = fp.read()
mystr = mybyte.decode('utf8')
fp.close()
# print(mystr)



