'''
@author:Maifeng
@file:kw.py
@time:2018/7/2下午5:57

'''
# -*- coding: utf-8 -*

from kw_api.kw_api import kw_api
from kw_api.kw_cmd import kw_search_input, kw_select_song_input


def kw_process():
    user_key = kw_search_input()
    if user_key:
        api = kw_api()
        songs = api.get_user_search(user_key)

        user_select = kw_select_song_input(songs)

        api.get_user_song(user_select)