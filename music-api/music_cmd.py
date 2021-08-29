'''
@author:Maifeng
@file:music_cmd.py
@time:2018/6/1716:48

'''
# -*- coding: utf-8 -*-


def music_output():
    print(
        '''
        作者:买峰
        时间:2018-6-18
        版本:1.0
        功能:下载各大平台音乐(网易,酷狗,酷我,QQ音乐)
        wx公众号:maifeng_cat
        请大家多多关注,觉得有用的可以给个赞.
        '''
    )

def select_input():
    user_cmd = input(
        '''
        请用户选择平台---- 比如: 选择网易--->输入0--->回车 
        网易------------0
        酷我------------1
        酷狗------------2
        腾讯------------3
        退出------------4
        \n
        '''
    )
    if user_cmd:
        return user_cmd
    else:
        print('请用户选择正确的标号')
        return select_input()