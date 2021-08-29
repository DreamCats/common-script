'''
@author:Maifeng
@file:kw_config.py
@time:2018/7/2下午5:57

'''
# -*- coding: utf-8 -*-

# 酷我 api

# 酷我搜索api

KW_SEARCH_URL = 'http://sou.kuwo.cn/ws/NSearch'

HEADERS_SEARCH = {
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Connection':'keep-alive',
    'Host':'sou.kuwo.cn',
    'Referer':'http://www.kuwo.cn/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie':'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1530515636; bdshare_firstime=1530515654324; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1530525226'
}


KW_GET_SONG_URL = 'http://antiserver.kuwo.cn/anti.s'

HEADERS_SONG = {
    'Host':'antiserver.kuwo.cn',
    'Referer':'http://www.kuwo.cn/yinyue/',
    'Range': 'bytes=0-',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie':'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1530515636; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1530527123'
}