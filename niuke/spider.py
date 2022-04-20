import requests, time
from pyquery import PyQuery as pq

ss = requests.session()

urls = [
    'https://www.nowcoder.com/discuss/tag/665-json?order=3&type=2&tagId=665&expTag=639&query=%E7%A4%BE%E6%8B%9B',
]

def time2str(value):
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(value // 1000))

def save_content(title, content):
    title = title.replace('/', '-')
    with open(f'datas/{title}.md', 'w', encoding='utf-8') as f:
        f.write(content)

def spider(url):
    resp = ss.get(url)
    datas = resp.json()['data']['discussPosts']
    for idx, value in enumerate (datas):
        url = f'https://www.nowcoder.com/discuss/{value["postId"]}'
        t = time2str(value['createTime'])
        title = value['postTitle'],
        title = title[0] if isinstance(title, tuple) else title
        resp = ss.get(url)
        doc = pq(resp.text)
        ct = doc('.post-topic-des')
        content = f'''[原文链接]({url})\n\n{title}\n\n## 时间:{t}\n\n## 内容:\n\n{ct.text()}'''
        print(title)
        save_content(title, content)

def run():
    page = 1
    for url in urls:
        for idx in range(1, page+1):
            url = url + f'&page={idx}'
            spider(url)



if __name__ == '__main__':
    run()
    print('end...')