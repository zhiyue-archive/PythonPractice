import urllib2
from bs4 import BeautifulSoup
import re

url="http://www.baidu.com/s?wd=cloga"
doc = urllib2.urlopen(url)
content = doc.read()
soup = BeautifulSoup(content)
