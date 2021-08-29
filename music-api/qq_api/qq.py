# -*- coding: utf-8 -*

from qq_api.qq_api import qq_api
from qq_api.qq_cmd import qq_search_input,  qq_select_song_input


def qq_process():
    user_key = qq_search_input()
    if user_key:
        api = qq_api()
        songs = api.get_user_search(user_key)
        user_select = qq_select_song_input(songs)
        api.get_user_song(user_select)