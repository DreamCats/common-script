'''
@author:Maifeng
@file:wy.py
@time:2018/6/1716:47

'''
# -*- coding: utf-8 -*-

from wy_api.wy_cmd import wy_search_input, wy_select_song_input
from wy_api.wy_api import wy_api

def wy_process():
    user_key = wy_search_input()
    if user_key:
        api = wy_api()
        songs = api.get_user_search(user_key)
        user_select = wy_select_song_input(songs)
        api.get_user_song(user_select)
