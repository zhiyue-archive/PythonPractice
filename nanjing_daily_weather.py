import urllib2 
from bs4 import BeautifulSoup
import re
url = 'http://www.weather.com.cn/weather1d/101190101.shtml'
response = urllib2.urlopen(url)  
content = response.read() 
soup = BeautifulSoup(content)
site = soup.find(id=re.compile("hidden_title"))['value']
print site




