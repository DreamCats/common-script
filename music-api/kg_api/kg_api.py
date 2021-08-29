'''
@author:Maifeng
@file:kg_api.py
@time:2018/6/30下午1:08

'''
# -*- coding: utf-8 -*-
import requests

from kg_api.kg_config import KG_SEARCH_URL, HEADERS_SEARCH, CALLBACK, SPLIT, HEADERS_SONG
from kg_api.kg_config import KG_GET_SONG_URL, KG_FILE_PATH


class kg_api(object):
    def __init__(self):
        super(kg_api, self).__init__()

        self.search_url = KG_SEARCH_URL

        self.song_url = KG_GET_SONG_URL
        self.headers_search = HEADERS_SEARCH

        self.headers_song = HEADERS_SONG
        self.s = requests.session()

    def get_user_search(self, user_key):
        if user_key:
            # jQuery112408817627034043487_1530340218370
            # jQuery1124028090183153670867_1530341691766
            # jQuery11240181100723525919_1530341711966
            params = {
                'callback': CALLBACK,
                'keyword': user_key,
                'page': '1',
                'pagesize': '30',
                'userid': -1,
                'clientver':'',
                'platform': 'WebFilter',
                'tag': 'em',
                'filter': 2,
                'iscorrection': 1,
                'privilege_filter': 0,
                '_': 1530341711966,
            }
            user_songs = []
            try:
                response_search = self.s.get(self.search_url, headers=self.headers_search, params=params)

                if response_search.status_code == 200:
                    results = response_search.text + SPLIT
                    results = eval(response_search.text.split(CALLBACK)[1].split(SPLIT)[0])
                    songs = results['data']['lists']
                    for i, song in enumerate (songs):
                        name = song['SongName']
                        ID = song['AlbumID']
                        author = song['FileName']
                        file_hash = song['FileHash']
                        info = {
                            'num': i,
                            'name': name,
                            'ID': ID,
                            'author': author,
                            'file_hash':file_hash,
                        }
                        user_songs.append(info)
                    return user_songs
                else:
                    return None
            except Exception as e:
                print('get_user_search', e)
                return None
        else:
            return None


    def get_user_song(self, user_song):
        if user_song:
            ID = user_song['ID']
            name = user_song['name']
            if 'em' in name:
                name = name.split('<em>')[1].split('<')[0]
            file_hash = user_song['file_hash']
            params = {
                'r': 'play/getdata',
                'hash': file_hash,
                'album_id': ID,
                '_': 1530418907171,
            }
            resp_index = self.s.get(self.song_url, params=params, headers=self.headers_song)
            if resp_index.status_code == 200:
                song_url = resp_index.json()['data']['play_url']
                if song_url:

                    try:
                        resp_song = self.s.get(song_url)
                        if resp_song.status_code == 200:
                            self.save(name, resp_song.content)
                        else:
                            return None
                    except Exception as e:
                        print('download fail:',e)
                else:
                    return None
            else:
                return None

    def save(self, file_name, content):
        with open(file_name + '.mp3', 'wb') as f:
            f.write(content)
            print('下载成功:',file_name)



if __name__ == '__main__':
    api = kg_api()
    api.get_user_search('不仅仅是喜欢')