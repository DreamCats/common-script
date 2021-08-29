'''
@author:Maifeng
@file:wy_config.py
@time:2018/6/1716:47

'''
# -*- coding: utf-8 -*-



# 网易云 api


# 网易云下载api
WY_DOWNLOAD_URL = 'http://music.163.com/song/media/outer/url?id='

# https://music.163.com/#/search/m/?s=小半&type=1

# 网易云搜索api
WY_SEARCH_URL = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

# 网易云头

HEADERS = {
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Connection':'keep-alive',
    'Host':'music.163.com',
    'Referer':'http://music.163.com/search/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Cookie':'usertrack=ezq0plpPWPe//gV2BZcWAg==; _ntes_nnid=e40cba031e9c1e9c73892253c7142414,1515149562580; _ntes_nuid=e40cba031e9c1e9c73892253c7142414; _ga=GA1.2.1728819992.1515149568; _iuqxldmzr_=32; nts_mail_user=maifeng_hy@163.com:-1:1; __f_=1521599444872; P_INFO=maifeng_hy@163.com|1523761297|0|other|00&99|sic&1520484050&mail163#sic&510100#10#0#0|&0||maifeng_hy@163.com; __e_=1525400595432; WM_TID=%2FxnDWozaDIsd%2BtYo2%2FNOW57L6VMq9%2F3o; __utma=94650624.1728819992.1515149568.1528729337.1529234756.8; __utmc=94650624; __utmz=94650624.1529234756.8.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=FXPwJuN%2FqEim3m8BhWMh5wmy6Bz2tXjI2mJbfOzR%5Ccb9bED%5CuuJIyZkwb8we5AezC%2B7l4RP%2FgUiETANik7BNoNnPFukKkGFWMZSqOi1g2uBjUwq3vqNi1pcxGiOTdicJh%2FiZ%2F8iEVqFkrWtEPWMEn%2FZ7A442TIv%5CRB92U8VXvqmDHwth%3A1529238295524; __utmb=94650624.13.10.1529234756'
}

# 存储路径

WY_FILE_PATH = './'  # 当前路径
