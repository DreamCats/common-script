'''
@author:Maifeng
@file:kg_config.py
@time:2018/6/30下午1:08

'''
# -*- coding: utf-8 -*-

# 酷狗api



# 酷狗搜素api
KG_SEARCH_URL = 'http://songsearch.kugou.com/song_search_v2'



# 获取歌曲的url
KG_GET_SONG_URL = 'http://www.kugou.com/yy/index.php'


# 酷狗头

HEADERS_SEARCH = {
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Connection':'keep-alive',
    'Host':'songsearch.kugou.com',
    'Referer':'http://www.kugou.com/yy/html/search.html',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie':'kg_mid=e10f02f7d80532490114196d11b1ad1d; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1530337535; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1530337555'
}

HEADERS_SONG = {
    'Host':'www.kugou.com',
    'Referer':'http://www.kugou.com/song/',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie':'kg_mid=e10f02f7d80532490114196d11b1ad1d; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1530337535; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1530418893'
}
# 回调参数

CALLBACK = 'jQuery11240181100723525919_1530341711966'

SPLIT = '*'

# 存储路径

KG_FILE_PATH = './'  # 当前路径