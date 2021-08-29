'''
@author:Maifeng
@file:kw_api.py
@time:2018/7/2下午5:57

'''
# -*- coding: utf-8 -*-
import requests

from kw_api.kw_config import KW_SEARCH_URL, HEADERS_SEARCH, HEADERS_SONG, KW_GET_SONG_URL
from pyquery import PyQuery as pq

class kw_api(object):
    def __init__(self):
        super(kw_api, self).__init__()

        self.search_url = KW_SEARCH_URL

        self.song_url = KW_GET_SONG_URL
        self.headers_search = HEADERS_SEARCH

        self.headers_song = HEADERS_SONG
        self.s = requests.session()

    def get_user_search(self, user_key):
        if user_key:
            params = {
                'type': 'all',
                'catalog': 'yueku20177',
                'key': user_key
            }
            user_songs = []
            try:
                resp_search = self.s.get(self.search_url, params=params, headers=self.headers_search)
                if resp_search.status_code == 200:
                    results = resp_search.text

                    doc = pq(results)
                    songs =doc('.list ul li').items()

                    for i, song in enumerate (songs):

                        song_id = song('.number input').attr('value')

                        ID = song_id
                        name = song('.m_name a').attr('title')
                        author = song('.s_name a').attr('title')
                        info = {
                            'num': i,
                            'name': name,
                            'ID': ID,
                            'author': author,
                        }

                        user_songs.append(info)
                    return user_songs
                else:
                    return None
            except Exception as e:
                print('get_user_search:', e)
                return None
        else:
            return None
    def get_user_song(self, user_song):
        if user_song:
            ID = user_song['ID']
            song_id = 'MUSIC_' + ID
            name = user_song['name']
            params = {
                'format': 'aac|mp3',
                'rid': song_id,
                'type': 'convert_url',
                'response': 'res'
            }

            self.headers_song['Referer'] = self.headers_song['Referer'] + ID + '/'

            resp_song = self.s.get(self.song_url, params=params, headers=self.headers_song)
            resp_song = self.s.get(resp_song.url)
            self.save(name, resp_song.content)
        else:
            return None


    def save(self, file_name, content):
        with open(file_name + '.mp3', 'wb') as f:
            f.write(content)
            print('下载成功:',file_name)