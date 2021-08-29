'''
@author:Maifeng
@file:music.py
@time:2018/6/1716:45

'''
# -*- coding: utf-8 -*-
from kw_api.kw import kw_process
from music_cmd import music_output, select_input
from wy_api.wy import wy_process
from kg_api.kg import kg_process
from qq_api.qq import qq_process






def main():
    music_output()
    user_cmd = select_input()
    while True:
        if user_cmd == '0':
            wy_process()
        if user_cmd == '2':
            kg_process()
        if user_cmd == '1':
            kw_process()
        if user_cmd == '3':
            qq_process()
        if user_cmd == '4':
            exit()
        else:
            print('老老实实选择正确的序号吧......')
            user_cmd = select_input()


if __name__ == '__main__':
    main()