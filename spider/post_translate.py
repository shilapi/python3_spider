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
    'i':'你好',
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
}

response = requests.post(url,headers=headers,data=form_data)
print (response.json())
content = json.loads(response.text)
print(content)
