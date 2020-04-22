import requests
from bs4 import BeautifulSoup

#筛选出需要的内容并加上序号，存为列表
def findtarget (s,head,end) :
    re = []
    if isinstance(s,list) :
        for t in range(len(s)):
            l = str(s[t])
            headnum = l.find(head) + len(head)
            endnum = l.find(end)
            re.append(str(t+1)+'.'+l[headnum:endnum])
    return re
#爬取的链接地址
url = "https://www.bilibili.com/ranking"
'''
headers = {
    'User-Agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
}
'''
indexurl = requests.get(url)
strtext = indexurl.text
#print(strtext)
soup = BeautifulSoup(strtext,'lxml')
#获取指定字符串，保存为list
data = soup.select('#app > div.b-page-body > div > div.rank-container > div.rank-body > div.rank-list-wrap > ul > li > div.content > div.info > a')
print(data)
result = findtarget(data,'target="_blank">','</a>')
print('\n'.join(result))
