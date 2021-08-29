
# -*- coding: utf-8 -*-
import requests
import re
import json
from pyquery import PyQuery as pq
from qq_api.qq_config import QQ_SEARCH_URL, HEADERS_SEARCH, QQ_HTML_URL, HEADERS_HTML, QQ_SONG_URL ,HEADERS_SONG, HEADERS_DOWNLOAD

class qq_api(object):
    def __init__(self):
        super(qq_api, self).__init__()

        self.search_url = QQ_SEARCH_URL
        self.html_url  = QQ_HTML_URL
        self.song_url = QQ_SONG_URL
        self.headers_search = HEADERS_SEARCH
        self.headers_html  = HEADERS_HTML
        self.headers_song = HEADERS_SONG
        self.headers_download = HEADERS_DOWNLOAD
        self.s = requests.session()

    def get_user_search(self, user_key):
        if user_key:
            params = {
                'ct':'24',
                'qqmusic_ver':'1298',
                'new_json':'1',
                'remoteplace':'txt.yqq.song',
                'searchid':'68044557041319643',
                't':'0',
                'aggr':'0',
                'cr':'1',
                'catZhida':'1',
                'lossless':'0',
                'flag_qc':'0',
                'p':'1',
                'n':'20',
                'w':user_key,
                'g_tk':'698409247',
                'jsonpCallback':'MusicJsonCallback0061442364123023285',
                'loginUin':'0',
                'hostUin':'0',
                'format':'jsonp',
                'inCharset':'utf8',
                'outCharset':'utf-8',
                'notice':'0',
                'platform':'yqq',
                'needNewCode':'0'

            }
            user_songs = []
            try:
                response_search = self.s.get(self.search_url, headers=self.headers_search, params=params)
                if response_search.status_code == 200:
                    response_search.encoding = 'utf-8'
                    # content = re.compile('MusicJsonCallback0061442364123023285\((.*?)\)').findall(response_search.text)
                    content = (response_search.text.split('MusicJsonCallback0061442364123023285(')[1] + 'flag').split(')flag')[0]
                    content = json.loads(content)
                    data = content.get('data')
                    songs = data.get('song').get('list')
                    for i, song in enumerate (songs):
                        name = song.get('title')
                        author = song.get('singer')[0].get('name')
                        song_mid = song.get('mid')
                        info = {
                            'num': i,
                            'name': name,
                            'author': author,
                            'song_mid':song_mid,
                        }
                        user_songs.append(info)
                    return user_songs
                else:
                    return None
                    
            except Exception as e:
                print(e)
        else:
            return None

    def get_vkey(self, songmid, songname):
        if songmid and songname :
            params = {
                'g_tk': '5381',
                'jsonpCallback': 'MusicJsonCallback8571665793949388',
                'loginUin': '0',
                'hostUin': '0',
                'format': 'json',
                'inCharset': 'utf8',
                'outCharset': 'utf-8',
                'notice': '0',
                'platform': 'yqq',
                'needNewCode': '0',
                'cid': '205361747',
                'callback': 'MusicJsonCallback8571665793949388',
                'uin': '0',
                'songmid': songmid,
                'filename': 'C400'+ songmid + '.m4a',
                'guid': '7133372870'
            }
            try:
                response_vkey = self.s.get(self.song_url, headers=self.headers_song, params=params)
                if response_vkey.status_code == 200:
                    response_vkey.encoding = 'utf-8'
                    vkey_disc = re.compile('MusicJsonCallback8571665793949388\((.*?)\)').findall(response_vkey.text)[0]
                    vkey_disc = json.loads(vkey_disc)
                    data = vkey_disc['data']
                    items = data.get('items')[0]
                    vkey = items.get('vkey')                  
                    self.get_music(vkey, songname,'C400'+ songmid + '.m4a')
                else:
                    return None
            except Exception as e:
                print(e)
        else:
            return None

    def get_user_song(self, user_song):
        if user_song:
            song_mid = user_song['song_mid']
            song_name = user_song['name']
            self.get_vkey(song_mid, song_name)  
        else:
            return None
            
    def get_music(self,vkey,songname,filename):
        if vkey and songname:
            download_url = 'http://dl.stream.qqmusic.qq.com/' + filename + '?vkey=' + vkey + '&guid=7133372870&uin=0&fromtag=66'
            music = requests.get(download_url, headers=self.headers_download).content
            with open(songname + '.m4a', 'wb') as f:
                f.write(music)
            print('下载成功:',songname)
