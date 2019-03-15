# __author__: Mai feng
# __file_name__: speaking_infom.py
# __time__: 2019:03:08:17:50


# 配置邮箱信息
import smtplib
from email.mime.text import MIMEText
from email.header import Header
class EmailConfig:
    def __init__(self):
        # 配置邮箱信息
        self.smtpserver = "smtp.qq.com"
        self.smtpport = 465
        self.from_mail = "470957137@qq.com"
        # self.to_mail = ["maifeng_cat@qq.com", 
        # '1647005988@qq.com', 
        # '249818110@qq.com', 
        # '1229245203@qq.com',
        # 'maifeng868@gmail.com']
        self.to_mail = ['maifeng_cat@qq.com']
        self.password = ''


    def send_mail(self):
        '''
        '''
        msg = MIMEText('速度去微信公众号选择心仪的口语访老师...', 'plain', 'utf-8')
        msg['From'] = '470957137@qq.com'
        msg['To'] = '470957137@qq.com'
        subject = '口语访通知...'
        msg['Subject'] = Header(subject, 'utf-8')
        try:
            smtp = smtplib.SMTP_SSL(self.smtpserver, self.smtpport)
            # smtp = smtplib.SMTP()
            # smtp.connect(self.smtpserver, self.smtpport)
            smtp.login(self.from_mail,self.password)
            smtp.sendmail(self.from_mail,self.to_mail,msg.as_string())
            print('send success！！！')
        except Exception as e:
            print('send_mail->', e)


# config 配置信息

class Config:
    # 学号：
    username = '' 
    # 密码
    password = ''
    # 周期
    periods = 120 # 暂定三分钟 
    # 口语访服务器崩溃周期
    periods_errors = 600 # 暂定十分钟 
    # 口语访次数
    speaking_count = 3 # 这个可是要经常修改的


import requests, time, datetime
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
        # self.headers = {'Cookie':'think_language=zh-cn; PHPSESSID=9p2tgnef8bejdb4km3j80lb1p3'}
        self.headers = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1',
        }
        


        # post_login_url 
        self.post_login_url = 'http://epc.uestc.edu.cn/index.php/Wechat/User/ajax_login'

        # speaking_item_url 
        self.speaking_item_url = 'http://epc.uestc.edu.cn/index.php/Wechat/Display/index/country_id/389'

        # form-data
        self.form_data = {'phone':self.config.username, 'password':self.config.password}

        # requests.session()
        self.s = requests.session()
        
        # 初始化 url
        self.init_url = 'http://epc.uestc.edu.cn/index.php/init'

        # sure_url
        self.sure_url = 'http://epc.uestc.edu.cn/index.php/Wechat/Other/confirm_disclaimer/back_url/display_index'

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
            
            # 初始化
            res = self.s.get(url=self.init_url, headers=self.headers)
            res = self.s.post(url=self.sure_url, headers=self.headers)
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
                    print('账号密码异常，或者去口语访公众号激活该cookie ', datetime.datetime.now())
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
                    # print(item)
                # 判断是用户想要的
                print('目前口语访是第%d周' %len(amount))
                print('用户需要第%d周口语访' %self.config.speaking_count)
                if len(amount) == self.config.speaking_count:
                    # 代表开始发邮箱了。
                    for item in amount:
                        print(item)
                    email = EmailConfig()
                    email.send_mail()
                    return result
                else:
                    print('没有达到用户的要求...', datetime.datetime.now())
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
            if res == '2':
                # 说明口语访次数未到达要求...那么
                time.sleep(self.config.periods)
                return self.process()
        elif res == '2':
            time.sleep(self.config.periods)
            return self.process()
        else:
            print('对面服务器崩溃了...  ', datetime.datetime.now())
            time.sleep(self.config.periods_errors)
            return self.process()



if __name__ == "__main__":
    speakingInform = SpeakingInform(Config)
    speakingInform.process()
    # email = EmailConfig()
    # email.send_mail()
