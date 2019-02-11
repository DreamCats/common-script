# __author__: Mai feng
# __file_name__: lmy_video.py
# __time__: 2019:02:09:21:40

import requests, re
from pyquery import PyQuery as pq

class Config:
    username = ''
    password = ''

    login_url = 'https://www.mosoteach.cn/web/index.php?c=passport&m=account_login'
    
    # 主页
    index_url = 'https://www.mosoteach.cn/web/index.php?c=clazzcourse&m=index'
    # 视频主页资源
    video_url = 'https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id={course_id}'
    # 视频post网址
    watch_url = 'https://www.mosoteach.cn/web/index.php?c=res&m=save_watch_to'
    
    

class LmyVideo(object):
    def __init__(self, config):
        self.config = config
        self.s  = requests.session()

    def start(self):
        self.login()
        index_infos = self.get_index()
        user_course_id = self.get_user_index(index_infos)
        video_infos = self.get_video_resource(user_course_id)
        self.parse_video(video_infos)
       

    def login(self):
        '''登录方法
        '''
        login_datas  = {'account_name':self.config.username, 'user_pwd':self.config.password, 'remember_me': 'N'}
        try:
            res_login = self.s.post(url=self.config.login_url, data=login_datas)
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
            return None

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
            
    def get_user_index(self, index_infos):
        '''与用户交互，得到用户的选择
        :param index_infos: 主页课程列表
        :return: 待定
        '''
        for index_info in index_infos:
            prt_index = '序号：{id} --- 名称：{name} \n'.format(id=index_info['item_id'], name=index_info['data_name'])
            print(prt_index)
        user_cmd = input('请用户选择相应的序号......\n')
        if user_cmd:
            return index_infos[int(user_cmd)]['data_id']
        else:
            return self.get_user_index(index_info)

    def get_video_resource(self, course_id):
        '''获取视频主页资源
        :param course_id: 课程id
        :return: items_list:
                    {
                        'data_value',
                        'video_time',
                        'course_id',
                    }
        '''
        index_url = self.config.video_url.format(course_id=course_id)
        try:
            res_video_index = self.s.get(url=index_url)
            if res_video_index.status_code == 200:
                doc = pq(res_video_index.text)
                items = doc('.res-row-open-enable').items()
                items_list = []
                for item in items:
                    if item.attr('data-mime') == 'video':
                        data_value = item.attr('data-value')
                        # print('视频id:',data_value)
                        video_time = re.findall(r'.*?<span>(.*?) 分钟</span>.*?',str(item('.create-box')))[0]
                        is_green = True if 'color:#8fc31f' in str(item('.create-box')) else False
                        if is_green:
                            print(data_value + '已经获取视频经验')
                            continue
                        # print('视频时间:', video_time)
                        items_list.append(
                            {
                                'data_value':data_value,
                                'video_time':video_time,
                                'course_id':course_id
                            }
                        )
                    else:
                        continue
                return items_list
            else:
                return None
        except Exception as e:
            print('get_video_resource->', e)

    def parse_video(self, video_infos):
        '''根据视频信息，post视频信息
        :param video_infos: 视频信息列表
        :return: 待定
        '''
        try:
            if video_infos:
                for video_info in video_infos:
                    video_time_min = int((float(video_info['video_time']) - 0.05) * 60)
                    for count in range(video_time_min, video_time_min + 7):
                        watch_datas = {
                            'clazz_course_id':video_info['course_id'],
                            'res_id':video_info['data_value'],
                            'watch_to':video_time_min + count,
                            'duration':video_time_min + count,
                            'current_watch_to':0
                        }
                        res_watch = self.s.post(url=self.config.watch_url, data=watch_datas)
                        if res_watch.status_code == 200:
                            print(video_info['data_value']+'视频经验获得成功...---->',res_watch.text)
                        else:
                            return None
            else:
                return None
        except Exception as e:
            print('parse_video->', e)
            return None

def main():
    username = input('请输入账号：')
    password = input('请输入密码：')
    config = Config()
    config.username = username
    config.password = password
    lmy_video = LmyVideo(config)
    lmy_video.start()


if __name__ == "__main__":
    main()