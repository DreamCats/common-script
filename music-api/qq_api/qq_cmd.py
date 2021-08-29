def qq_search_input():
    user_cmd = input(
        '''
        请用户输入搜索关键词:

        '''
    )
    if user_cmd:
        return user_cmd
    else:
        print('请用户正确输入关键词')
        return qq_search_input()



def qq_select_song_input(songs):
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
                print('请用户正确输入关键词', e)
                return qq_select_song_input(songs)
        else:
            print('请用户正确输入关键词')
            return qq_select_song_input(songs)
    else:
        return None