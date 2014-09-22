import urllib2 
from bs4 import BeautifulSoup
import re
import string
import sys


def OnlyCharNum(s,oth=''):
	    s2 = s.lower();
	    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
	    for c in s2:
	        if not c in fomart:
	            s = s.replace(c,'');
	    return s;


if __name__=='__main__':
        myname=raw_input("请输入姓名\n")
        keywordsnum=raw_input("请输入关联词个数\n")
        if int(keywordsnum) == 0:
                keywords=[myname]
        else:
                keywords=['']*int(keywordsnum) 
                for k in range(int(keywordsnum)):
                    keywords[k]=raw_input("请输入关联的关键字%d\n"%(k+1))
        url1 = "http://www.baidu.com/s?wd="+myname
        response1 = urllib2.urlopen(url1)  
        content1 = response1.read() 
        soup1 = BeautifulSoup(content1)
        site1 = soup1.find(class_="nums").get_text()
        num = string.atoi(OnlyCharNum(site1[11:-1].strip() .lstrip() .rstrip(',')))
        page = num/10
        print num,page
        filename=myname+".txt"
        myfile=open(filename,"w")
        keywordshownum=0
        
        for i in range(int(page)):
                url="http://www.baidu.com/s?wd="+myname+"&pn=%d"%(10*i)
                print ('Page：%d/%d/%d'%((i+1),(int)(page),(keywordshownum)))
                response = urllib2.urlopen(url)  
                content =response.read() 
                soup = BeautifulSoup(content)
                sites = soup.find_all(class_="c-abstract")	#find_all返回的是list，find返回的是obj
                pretext=' '.encode('gb18030')
                for site in sites:
                        text = site.get_text().encode('gb18030')
                        if cmp(text,pretext) == 0:
                            break
                        else:
                            pretext=text
                            myfile.write(text)
                            for keyword in keywords:
                                if keyword in text:
                                    print text
                                    keywordshownum=keywordshownum+1
                                    break

        myfile.close()  


'''

'''
'''

'''
