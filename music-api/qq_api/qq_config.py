# -*- coding: utf-8 -*-

# qq api


# qq搜素api
QQ_SEARCH_URL = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

QQ_HTML_URL = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg'

QQ_SONG_URL = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg'



# qq头

HEADERS_SEARCH = {

    'Referer':'https://y.qq.com/portal/search.html',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

HEADERS_HTML = {

    'Referer':'https://y.qq.com/n/yqq/singer/003aQYLo2x8izP.html',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

HEADERS_SONG = {

    'Referer':'https://y.qq.com/portal/player.html',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
HEADERS_DOWNLOAD = {
    'referer': 'https://y.qq.com/n/yqq/singer/003aQYLo2x8izP.html',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}