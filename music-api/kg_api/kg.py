'''
@author:Maifeng
@file:kg.py
@time:2018/6/30下午1:08

'''
# -*- coding: utf-8 -*-
from kg_api.kg_api import kg_api
from kg_api.kg_cmd import kg_search_input, kg_select_song_input


def kg_process():
    user_key = kg_search_input()
    if user_key:
        api = kg_api()
        songs = api.get_user_search(user_key)
        user_select = kg_select_song_input(songs)
        api.get_user_song(user_select)