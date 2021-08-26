# __author__: Mai feng
# __file_name__: notify_lc.py
# __time__: 2021:07:24:22:15

import requests, random, schedule, time

ss = requests.session()

page_end = 17
token = '' # https://pushplus.hxtrip.com/
encoder = 'lc'
notify_num = 3
post_time = "08:00"

lc_base_url = 'https://leetcode-cn.com/graphql/'
query_val = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    hasMore
    total
    questions {
      acRate
      difficulty
      freqBar
      frontendQuestionId
      isFavor
      paidOnly
      solutionNum
      status
      title
      titleCn
      titleSlug
      topicTags {
        name
        nameTranslated
        id
        slug
      }
      extra {
        hasVideoSolution
        topCompanyTags {
          imgUrl
          slug
          numSubscribed
        }
      }
    }
  }
}
    """
items = []

send_mq_url = 'http://pushplus.hxtrip.com/send'

store_map = {}

def get_lc_list_post(current_page):
    datas = {
        'operationName': "problemsetQuestionList",
        'query': query_val,
        'variables': {
            'categorySlug': "",
            'filters': {},
            'limit': 50,
            'skip':current_page * 50
        }
    }
    resp = ss.post(url=lc_base_url, json=datas)
    datas = resp.json()['data']['problemsetQuestionList']
    questions = datas['questions'] # list
    for q in questions:
        if q['solutionNum'] < 500:
            continue
        if q['difficulty'] == "HARD":
            continue
        item = {
            'difficulty': q['difficulty'],
            'id': q['frontendQuestionId'],
            'number': q['solutionNum'],
            'title': q['titleCn']
        }
        items.append(item)

def notify_user():
    # 打乱列表
    random.shuffle(items)
    # 取前3个
    datas = get_random_datas(items)
    print(datas)
    # 通知
    post_data = {
        'token': token,
        'title': '买老师：每日8点推送3道leetcode，包含简单和中等',
        'content': str(datas),
        'template': 'json',
        'topic': encoder
    }
    resp = ss.post(url=send_mq_url, json=post_data)
    print('消息发送成功：' + resp.text)
    print(len(items), store_map)
  
def get_random_datas(lc_itmes):
    datas = []
    p = 0
    while p < 3:
        if store_map.get(lc_itmes[p]['id']):
            continue
        else:
            store_map[items[p]['id']] = 0
            datas.append(lc_itmes[p])
            p = p+1
    return datas


def run():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    for i in range(page_end):
        get_lc_list_post(i)
    notify_user()
    items.clear()



if __name__=="__main__":
    print("你们好，欢迎使用每日推送leetcode脚本...")
    schedule.every().day.at(post_time).do(run)
    while True:
        schedule.run_pending()   # 运行所有可以运行的任务
        time.sleep(2) 



