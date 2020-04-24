import requests
from bs4 import BeautifulSoup
import json
import time
import math
import random
import hashlib

input="你好"
ts=math.floor(time.time()*1000)
salt=ts*10+math.floor(random.random() * 10)
browserv='5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
bv=hashlib.md5((browserv).encode('utf-8')).hexdigest()
sign=hashlib.md5(("fanyideskweb" + input + str(salt) + "Nw(nmmbP%A-r6U3EUn]Aj").encode('utf-8')).hexdigest()
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
form_data={
    'i':input,
    'from':'zh-CHS',
    'to':'en',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': bv,
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'Referer': 'http://fanyi.youdao.com/',
    'cookies':'___rl__test__cookies:1587711594418; OUTFOX_SEARCH_USER_ID_NCOO:1537631300.1306639; OUTFOX_SEARCH_USER_ID:-987467867@10.169.0.82; JSESSIONID:aaaYoxK7YwO7Xc-GkSQgx',
}

response = requests.post(url,data=form_data)
#print (response)
req=requests.urlopen
html = response.read().decode('utf-8')
content = json.loads(html)
print(content['translateResult'][0][0]['tgt'])

