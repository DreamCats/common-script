'''
@author:Maifeng
@file:test.py
@time:2018/6/30下午1:55

'''
# -*- coding: utf-8 -*-
from qq_api.qq_api import qq_api

def main():
    qq = qq_api()
    songs = qq.get_user_search('放开')
    

if __name__ == '__main__':
    main()