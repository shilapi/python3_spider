import time, math, random,hashlib# 都是自带的模块
import requests
import urllib
import os
from bs4 import BeautifulSoup

def findtarget (s,head,end,headurl,endurl) :#筛选出需要的内容并加上序号，存为列表
    if isinstance(s,list) :
        for t in range(len(s)):
            l = str(s[t])
            dir = '/Users/shilapi/Documents/GitHub/python3_spider/spider/picdownload/'
            if not os.path.exists(dir):
                os.makedirs(dir)
            name=''
            urlpic=''
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
                }
            headnum = l.find(head) + len(head)+11
            endnum = l.find(end)
            headurlnum = l.find(headurl) + len(headurl)
            endurlnum = l.find(endurl)
            name=str(l[headnum:endnum])
            urlpic=str(l[headurlnum:endurlnum])
            file = 'picdownload/'+name  #下载文件
            #print(os.getcwd())
            #print(name)
            urllib.request.urlretrieve(url = urlpic,filename = file)

#爬取的链接地址
url = "https://www.jdlingyu.mobi/collection/meizitu"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
}

indexurl = requests.get(url,headers=headers)
strtext = indexurl.text
#print(strtext)
soup = BeautifulSoup(strtext,'lxml')

data = soup.select('#main > div.grid-bor > div > div > div.thumb.pos-r > div')#获取指定字符串，保存为list
print(data)
urlhead = "background-image:url('"
urlend = "')"
head = "background-image:url('http://img.jdlingyu.net/images/"
end = "')"
result = findtarget(data,head,end,urlhead,urlend)
#print('\n'.join(result))
