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
        # '7D49841E-AE74-11E8-AA22-7CD30AD36C02', # 英语id
        # '8D8A9E92-F137-11E8-832A-EC0D9ACEE976', # test_id
        # '03C0CDC4-F242-11E8-832A-EC0D9ACEE976', # 英语口语房
    ]
    base_url = 'https://www.mosoteach.cn/web/index.php' # lmy web_url
    login_url = 'https://www.mosoteach.cn/web/index.php?c=passport&m=account_login'
    # 登录post参数
    login_datas  = {'account_name':username, 'user_pwd':password, 'remember_me': 'N'}
    # 主页
    index_url = 'https://www.mosoteach.cn/web/index.php?c=clazzcourse&m=index'
    

class LmyVideo(object):
    def __init__(self, config):
        self.config = config
        self.s  = requests.session()

    def start(self):
        self.login()
        self.get_index()
       

    def login(self):
        '''登录方法
        '''
        try:
            res_login = self.s.post(url=self.config.login_url, data=self.config.login_datas)
            if res_login.status_code == 200:
                if res_login.json()['result_msg'] == 'OK':
                    print('登陆成功...')
                    # print(res_login.json())
                    return res_login.json()
                else:
                    print('登陆失败，账号密码错误...')
            else:
                return None
        except Exception as e:
            print('异常:login->', e)

    def get_index(self):
        '''获取主页
        :return: items_list:
                {
                    item_id,
                    data_id,
                    data_url,
                    data_name
                }
        '''
        try:
            res_index = self.s.get(url=self.config.index_url)
            if res_index.status_code == 200:
                doc = pq(res_index.text)
                # 用户课程列表
                items = doc('.clazzcourse-list-row').items()
                items_list = []
                for i, item in enumerate(items):
                    item_id = i
                    data_id = item.attr('data-id')
                    data_url = item.attr('data-url')
                    data_name = item('.clazzcourse-name').text()
                    items_list.append(
                        {
                            'item_id':item_id,
                            'data_id':data_id,
                            'data_url':data_url,
                            'data_name':data_name
                        }
                    )
                return items_list
            else:
                return None
        except Exception as e:
            print('get_index', e)
            


def main():
    lmy_video = LmyVideo(Config)
    lmy_video.start()


if __name__ == "__main__":
    main()