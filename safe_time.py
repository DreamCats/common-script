import requests
import time

s = requests.session()

url = 'http://222.197.182.137//exam_xuexi_online.php'

headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'wsess=ST-656796-yOm5fsuoEfxgGoo2QtBn1576721270565-amkN-cas',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

post_data = {
    'cmd':'xuexi_online'
}

while True:
    res = s.post(url, data=post_data, headers=headers)
    print(res.json())
    time.sleep(2)
    