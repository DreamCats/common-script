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
    speaking_count = 2 # 这个可是要经常修改的

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

        # speaking_item_url 
        self.speaking_item_url = 'http://epc.uestc.edu.cn/index.php/Wechat/Display/index/country_id/389'

        # form-data
        self.form_data = {'phone':self.config.username, 'password':self.config.password}

        # requests.session()
        self.s = requests.session()
        

    def login(self):
        '''登录功能
        :param null
        :return: result 
        '''
        try:
            # 返回状态
            # 0 代表成功
            # 1 代表状态码非200
            # 2 代表账号密码错误，或者账号不存在，或者需要在公众号激活该cookie
            # 3 代表异常
            result = '0'
            #  访问登录
            res = self.s.post(
                url=self.post_login_url,
                data=self.form_data,
                headers=self.headers
            )
            # 判断状态码是否是200
            if res.status_code == 200:
                if '登录成功' in res.json()['message']:
                    print(res.json()['message'])
                    return result
                else:
                    # 否则账号密码错误， 或者是号码不存在， 或者是需要公众号登录一下口语访激活该cookie
                    print('账号密码异常，或者去口语访公众号激活该cookie')
                    result = '2'
                    return result
            else:
                result = '1'
                return result
        except Exception as e:
            print('login->:',e)
            result = '3'
            return result

    def get_speaking_items(self):
        '''口语访周列表
        :param null
        :return: result
        '''
            # 返回状态
            # 0 代表成功
            # 1 代表状态码非200
            # 2 口语访周次数没有到达用户的要求。。。
            # 3 代表异常
        result = '0'
        try:
            res = self.s.get(
                url=self.speaking_item_url,
                headers=self.headers
            )
            if res.status_code == 200:
                doc = pq(res.text)
                items = doc('#area').items()
                amount = []
                for item in items:
                    amount.append(item('.media-heading').text())
                # 判断是用户想要的
                if len(amount) == self.config.speaking_count:
                    # 代表开始发邮箱了。
                    print('给user发邮箱，告诉user，口语访多出了一周呀...')
                    return result
                else:
                    print('口语访次数未达到user的要求...')
                    result = '2'
                    return result

            else:
                result = '1'
                return result
        except Exception as e:
            print('get_speaking_items->', e)
            result = '3'
            return result



    def process(self):
        '''访问流程
        '''
        res = self.login()
        if res == '0':
            res = self.get_speaking_items()


if __name__ == "__main__":
    speakingInform = SpeakingInform(Config)
    speakingInform.process()
