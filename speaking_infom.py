# __author__: Mai feng
# __file_name__: speaking_infom.py
# __time__: 2019:03:08:17:50

# config 配置信息

class Config:
    # 学号：
    username = '201822090429' 
    # 密码
    password = '220031'
    # 周期
    periods = '180' # 暂定三分钟 
    # 口语访次数
    speaking_count = '2' # 这个可是要经常修改的

import requests
from pyquery import PyQuery as pq

# 口语访类
class SpeakingInform(object):
    '''口语访功能类
    '''
    def __init__(self, config):
        '''初始化
        :param config: 配置信息参数
        :return: null
        '''
        self.config = config # 配置信息

        # 口语访微信公众号头部信息， 最重要的是cookie
        self.headers = {'Cookie':'think_language=zh-cn; PHPSESSID=j203eat1hn1716tis91csrog74'}
        
        # post_login_url 
        self.post_login_url = 'http://epc.uestc.edu.cn/index.php/Wechat/User/ajax_login'

        # form-data
        self.form_data = {'phone':self.config.username, 'password':self.config.password}

        # requests.session()
        self.s = requests.session()
                
