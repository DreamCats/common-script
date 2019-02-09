# __author__: Mai feng
# __file_name__: lmy_video.py
# __time__: 2019:02:09:21:40

import requests, re
from pyquery import PyQuery as pq

class Config:
    username = '17608037124'
    password = 'maifeng868'
    # 课程id
    course_id = [
        '0EF18A8D-B4E8-11E8-AA22-7CD30AD36C02', # 毛中特id
        # '7D49841E-AE74-11E8-AA22-7CD30AD36C02', # 英语id
        # '8D8A9E92-F137-11E8-832A-EC0D9ACEE976', # test_id
        # '03C0CDC4-F242-11E8-832A-EC0D9ACEE976', # 英语口语房
    ]
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'www.mosoteach.cn',
        'X-Requested-With':'XMLHttpRequest',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept':'application/json, text/javascript, */*; q=0.01',
    }
    base_url = 'https://www.mosoteach.cn/web/index.php' # lmy web_url
    login_params = {'c':'passport', 'm':'account_login'} # 登录url参数
    # 登录post参数
    login_datas  = {'account_name':username, 'user_pwd':password, 'remember_me': 'N'}
    # 获取资源前的静态方法，获取params参数
    @staticmethod
    def get_resource_params(clazz_id):
        return {'c':'res', 'm':'index', 'clazz_course_id': clazz_id}
    # 秒看视频的url的参数
    watch_params = {'c':'res','m':'save_watch_to'}
    