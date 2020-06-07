# coding=utf-8
import requests
from bs4 import BeautifulSoup

#筛选出需要的内容并加上序号，存为列表
def findtarget (s,head,end,headurl,endurl,i) :
    re = []
    if isinstance(s,list) :
        for t in range(len(s)):
            l = str(s[t])
            headnum = l.find(head) + len(head)
            endnum = l.find(end)
            headurlnum = l.find(headurl) + len(headurl)
            endurlnum = l.find(endurl)
            re.append(str(t+i*50)+'.'+l[headnum:endnum]+'链接'+l[headurlnum:endurlnum])
    return re
#爬取的链接地址
lenth = 0
for i in range(0,189) :
    url = "http://zhongkao.xdf.cn/list_1016_"+str(i)+".html"
    '''
    headers = {
        'User-Agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
    }
    '''
    indexurl = requests.get(url)
    strtext = indexurl.text.encode('iso-8859-1').decode('utf-8')
    #print(strtext)
    soup = BeautifulSoup(strtext,'lxml')
    #获取指定字符串，保存为list
    data = soup.select('#li_list > li > a')
    #print(data)
    result = findtarget(data,'arget="_blank">','</a>','<a href="','" t',i)
    lenth=lenth+1
    print('\n'.join(result))