# __author__: Mai feng
# __file_name__: notify_know.py
# __time__: 2021:07:25:14:31


# 声明一下， 生成的json，这里不贴了，有兴趣的可以wx联系我
import requests, random, schedule, time, os, json
from os import walk
ss = requests.session()
send_mq_url = 'http://pushplus.hxtrip.com/send'
notify_num = 10
token = '' # 可以去plusplus申请
notify_type = 1 # 0 是前端，1是后端
knows = {
      '0': 'Java基础',
      '1': 'Java集合',
      '2': 'Java多线程',
      '3': 'JVM',
      '4': 'Spring',
      '5': 'MySQL',
      '6': 'Redis',
      '7': '计算机网络',
      '8': '操作系统',
      '9': '分布式',
      '10': 'js',
      '11': 'css',
      '12': 'html',
      '13': '浏览器',
      '14': 'Vue',
      '15': '计算机网络'
    }

def load_files():
    files_list = []
    for (root, dirs, files) in walk('./'):
        for f in files:
            if f.endswith('.md'):
                files_list.append(root + '/' + f)
    return files_list

def load_content(filename):
    with open(filename, 'r') as f:
        return f.read()


def gen_json():
    # 1. 加载文件
    files_list = load_files()
    items = []
    for f in files_list:
        # 构造数据
        title = f.split('/')[2].split('.md')[0]
        c_id = f.split('/')[1]
        num = f.split('/')[2].split('.')[0]
        item = {
            'c_id': c_id,
            # 'id': num,
            'title': title,
            'type': knows[str(c_id)],
            # 'content': load_content(f),
        }
        items.append(item)
    with open('./knows.json', 'w') as f:
        f.write(json.dumps({"datas":items}))

def load_datas():
    with open('./knows.json', 'r') as f:
        items = f.read()
        items = json.loads(items)
    return items['datas']

def get_random_items(items):
    # 打乱列表
    random.shuffle(items)
    datas = []
    cnt = 0
    for item in items:
        if notify_type == 0:
            if int(item['c_id']) < 9:
                continue
        else:
            if int(item['c_id']) > 9:
                continue
        datas.append(item)
        cnt += 1
        if cnt > notify_num:
            break
    return datas

def notify_users():
    items = load_datas()
    
    # 取前5个
    datas = get_random_items(items)
    print(datas)
    # 通知
    post_data = {
        'token': token,
        'title': '买老师：每日12点推送10道后端面经题目',
        'content': str(datas),
        'template': 'json',
        'topic': 'back'
    }
    resp = ss.post(url=send_mq_url, json=post_data)
    print('消息发送成功：' + resp.text)

def run():
    notify_users()

if __name__=="__main__":
    # gen_json()
    # load_datas()
    # run()
    print("你们好，欢迎使用每日推送后端面经脚本...")
    schedule.every().day.at("12:00").do(run)
    while True:
        schedule.run_pending()   # 运行所有可以运行的任务
        time.sleep(2) 
