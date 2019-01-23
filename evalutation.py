# __author__: Mai feng
# __file_name__: evalutation.py
# __time__: 2019:01:23:13:22


'''参数配置'''
class Config:
    # 需要修改账号密码
    username = ''
    password = ''
    # 头部
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    # 登录uestc的url链接
    login_url = 'http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal'
    # 登录的一些参数配置
    it = '#casLoginForm > input[type="hidden"]:nth-child(7)'
    dllt = 'userNamePasswordLogin'
    execution = 'e1s1'
    _eventId = 'submit'
    rmShown = '1'
    # 登录提交表单的url
    login_post_url = 'http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal'
    
    # 教学评价
    home_index = 'http://yjsjy.uestc.edu.cn/pyxx/jzsso/login'
    evaluation_index_url = 'http://yjsjy.uestc.edu.cn/pyxx/pygl/jxpj/index'
    # 匹配需要评价的链接
    re_s = '.*?onclick="edit\(\'(\d+)\'\);".*?'
    # 提交评教的url
    evaluation_post_url = 'http://yjsjy.uestc.edu.cn/pyxx/pygl/jxpj/save/'

import requests
from pyquery import PyQuery as pq
import re
class Evaluation():
    def __init__(self, config):
        '''初始化
        :param config: 一些配置参数
        '''
        self.config = config
        # 实例化requests.session
        self.s = requests.session()

    def login(self):
        '''登录方法
        :return: True:返回成功
                 None:账号密码错误
        '''
        try:
            res_login = self.s.get(self.config.login_url)
            if res_login.status_code == 200:
                doc = pq(res_login.text)
                it = doc(self.config.it).attr('value')
                post_datas = {
                    'username': self.config.username,
                    'password': self.config.password,
                    'lt':it,
                    'dllt': self.config.dllt,
                    'execution': self.config.execution,
                    '_eventId': self.config._eventId,
                    'rmShown': self.config.rmShown,
                }
                res_login = self.s.post(self.config.login_post_url, data=post_datas, headers=self.config.headers)
                doc = pq(res_login.text)
                if doc('title').text() == '电子科技大学信息门户':
                    print('登录成功')
                    return True
                else:
                    print('账号密码错误...')
                    return None
            else:
                return None
        except Exception as e:
            print('login->', e)
    
    def start_evaluation(self):
        '''开始评教
        :return: None:评教失败，否则成功
        '''
        try:
            # self.config.headers['Cookie'] = 'JSESSIONID=C99FD3686A9DB44BBCBB6C2629D51EDE.pyxx_server2;'
            # http://yjsjy.uestc.edu.cn/pyxx/pygl/jxpj/edit/518254

            res_index = self.s.get(self.config.home_index, headers=self.config.headers)
            if res_index.status_code == 200:
                res_index = self.s.get(self.config.evaluation_index_url, headers=self.config.headers)
                if res_index.status_code == 200:
                    re_res = re.findall(self.config.re_s, res_index.text, re.S)
                    if re_res:
                        for r in re_res:
                            print(r)
                            self.post_evaluation(r)
                    else:
                        print('全部已经评教完成...')
                else:
                    return None
            else:
                return None
        except Exception as e:
            print('start_evaluation->', e)

    def post_evaluation(self, course_id):
        '''提交表单
        :param course_id: 评教课程id
        '''
        try:
            post_datas = {
                'cjid':'',
                'zjjsbh':'',
                'qz':'0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.75',
                'zbdm':'1,1,1,1,1,2,2,3,3,4,4,4,5,5,5,5,5',
                'mxzbdm':'1,2,3,4,5,1,2,1,2,1,2,3,1,2,3,4,5',
                'zgtm':',,,',
                'zgtmid':'1,2,3,4',
                'id': course_id
            }
            res = self.s.post(self.config.evaluation_post_url, data=post_datas, headers=self.config.headers)
            if res.status_code == 200:
                print('评教成功...')
            else:
                return None
        except Exception as e:
            print('post_evalutation->', e)


def main():
    username = input('请输入学号:')
    password = input('请输入密码:')
    if username != None and password != None:
        config = Config
        config.username = username
        config.password = password
        evaluation = Evaluation(config)
        res = evaluation.login()
        if res:
            evaluation.start_evaluation()
        else:
            main()
    else:
        print('学号和密码不能为空...')
        return main()

if __name__ == "__main__":
    main()