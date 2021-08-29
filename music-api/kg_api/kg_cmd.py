'''
@author:Maifeng
@file:kg_cmd.py
@time:2018/6/30下午1:08

'''
# -*- coding: utf-8 -*-

def kg_search_input():
    user_cmd = input(
        '''
        请用户输入搜索关键词:

        '''
    )
    if user_cmd:
        return user_cmd
    else:
        print('请用户正确输入关键词')
        return kg_search_input()


def kg_select_song_input(songs):
    if songs:
        for song in songs:
            print('歌曲名字:{name}------歌手:{author}------序号:{num}'.format(name=song['name'],
                                                                      author=song['author'],
                                                                      num=song['num']))
        user_cmd = input(
            '''
            请用户选择序号:

            '''
        )
        if user_cmd:
            try:
                user_select = songs[int(user_cmd)]
                return user_select
            except Exception as e:
                print('请用户正确输入关键词')
                return kg_select_song_input(songs)
        else:
            print('请用户正确输入关键词')
            return kg_select_song_input(songs)
    else:
        return None