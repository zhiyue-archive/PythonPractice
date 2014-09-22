import urllib,urllib2,cookielib
from bs4 import BeautifulSoup

url="http://www.renren.com"
email=""         #username
icode=""
origURL="http://www.renren.com/home"
domain="renren.com"
captcha_type="web_login"
password=""     #password
rkey="0b11db93e8347df56a5f0bda3689f8af"
f=""

proxy_support = urllib2.ProxyHandler({'http':'http://www.renren.com'})
cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
opener = urllib2.build_opener(proxy_support,cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)
content = urllib2.urlopen(url)



postdata=urllib.urlencode({
    'email':email,
    'icode':icode,
    'origURL':origURL,
    'domain':domain,
    'captcha_type':captcha_type,
	'password':password,
	'rkey':rkey,
	'f':f
})

req = urllib2.Request(
	url = 'http://www.renren.com/ajaxLogin/login?1=1',
	data = postdata
)

result = urllib2.urlopen(req).read()
renrencontent=urllib2.urlopen("http://www.renren.com").read() 
soup = BeautifulSoup(renrencontent)

print soup.body#.find_all(class_="time-tip")
